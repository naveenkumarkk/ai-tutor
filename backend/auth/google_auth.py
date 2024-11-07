import os
import requests
from flask import Blueprint, redirect, request, session, url_for, jsonify
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from config import Config
from models import User, db
from utils import credentials_to_dict, save_token
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

google_bp = Blueprint('google_bp', __name__)

SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/userinfo.email']

# Initialize the Google OAuth flow
@google_bp.route('/login')
def google_login():
    flow = Flow.from_client_secrets_file(
        'client_secret.json', scopes=SCOPES)
    flow.redirect_uri = url_for('google_bp.google_auth_callback', _external=True)
    
    authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
    session['state'] = state
    return redirect(authorization_url)

@google_bp.route('/auth_callback')
def google_auth_callback():
    state = session.get('state')
    flow = Flow.from_client_secrets_file(
        'client_secret.json', scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('google_bp.google_auth_callback', _external=True)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials

    # Get user info from Google and store in database
    user_info = get_google_user_info(credentials)
    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(email=user_info['email'])
        db.session.add(user)
    
    user.google_token = credentials_to_dict(credentials)
    db.session.commit()

    return jsonify({"message": "Google authentication successful", "user": user.email})

def get_google_user_info(credentials):
    service = build('oauth2', 'v2', credentials=credentials)
    return service.userinfo().get().execute()

def get_google_tasks_service(user_google_token):
    creds = google.oauth2.credentials.Credentials(user_google_token)
    service = googleapiclient.discovery.build('tasks', 'v1', credentials=creds)
    return service