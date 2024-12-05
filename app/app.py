from flask import Flask, redirect, request, jsonify, render_template, url_for
import os
from config import Config
from auth.google_auth import google_bp 
from controller.chatgpt_controller import chatgpt_bp
from extensions import db,migrate

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_object(Config)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:.rlXI0}1mq}gf+(Gp$DGA7<%#-.7@study-beam.cluster-cdmkm2suy14g.eu-north-1.rds.amazonaws.com/studybeam"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(google_bp, url_prefix="/google")
app.register_blueprint(chatgpt_bp, url_prefix="/chatgpt")

@app.route("/")
@app.route("/login")
def index():
    return render_template("login.html")

@app.route("/callback")
def callback():
    params = request.args.to_dict()
    redirect_uri = url_for("google_bp.auth_callback", _external=True, **params)
    return redirect(redirect_uri)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
