from flask import (
    Blueprint,
    redirect,
    request,
    session,
    url_for,
    jsonify,
    render_template,
)
from google_auth_oauthlib.flow import Flow
import requests
from googleapiclient.discovery import build
from models import User
from extensions import db
from utils import credentials_to_dict, save_token
import google.oauth2.credentials
import googleapiclient.discovery
from datetime import datetime

google_bp = Blueprint("google_bp", __name__)

SCOPES = [
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/userinfo.email",
    "openid",
]


@google_bp.route("/login")
def google_login():
    flow = Flow.from_client_secrets_file("./backend/client_secret.json", scopes=SCOPES)
    flow.redirect_uri = url_for("callback", _external=True)
    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )
    session["state"] = state
    return redirect(authorization_url)


@google_bp.route("/callback")
def auth_callback():
    state = session.get("state")
    flow = Flow.from_client_secrets_file(
        "./backend/client_secret.json", scopes=SCOPES, state=state
    )
    flow.redirect_uri = url_for("callback", _external=True)
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    user_info = get_google_user_info(credentials)

    user = User.query.filter_by(email=user_info["email"]).first()
    if not user:
        user = User(
            first_name=user_info["given_name"],
            last_name=user_info["family_name"],
            email=user_info["email"],
            google_id=user_info["id"],
            profile_picture=user_info["picture"],
            verified_email=user_info["verified_email"],
            created_at=datetime.utcnow(),
        )
        db.session.add(user)
    else:
        user.first_name = user_info["given_name"]
        user.last_name = user_info["family_name"]
        user.profile_picture = user_info["picture"]
        user.verified_email = user_info["verified_email"]
        user.last_login = datetime.utcnow()
    token = credentials_to_dict(credentials)
    user.google_token = token
    session["google_token"] = token
    session["user_id"] = user.user_id
    db.session.commit()

    return redirect(url_for("chatgpt_bp.chatscreen", _external=True))


@google_bp.route("/logout")
def logout():
    access_token = session.get("google_token", {}).get("token")
    print(access_token)
    session.clear()
    if access_token:
        revoke_url = f"https://accounts.google.com/o/oauth2/revoke?token={access_token}"
        response = requests.post(revoke_url)
        if response.status_code == 200:
            print("Token revoked successfully.")
        else:
            print("Failed to revoke token:", response.text)

    return redirect(url_for("index", _external=True))


def get_google_user_info(credentials):
    service = build("oauth2", "v2", credentials=credentials)
    return service.userinfo().get().execute()


def get_google_tasks_service(user_google_token):
    creds = google.oauth2.credentials.Credentials(user_google_token)
    service = googleapiclient.discovery.build("tasks", "v1", credentials=creds)
    return service
