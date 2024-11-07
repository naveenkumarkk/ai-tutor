from flask import Flask
from config import Config
from extensions import db, migrate  # Import db and migrate from extensions
from auth.google_auth import google_bp
# from auth.ms_auth import ms_bp
from controller.chatgpt_controller import chat_with_gpt

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions with the app
db.init_app(app)
migrate.init_app(app, db)

# Register authentication blueprints
app.register_blueprint(google_bp, url_prefix='/google')
# app.register_blueprint(ms_bp, url_prefix='/ms')

# Define routes
@app.route('/chat', methods=['POST'])
def chat_route():
    return chat_with_gpt()  # Use the separated ChatGPT controller

@app.route('/')
def index():
    return "Welcome to the AI Tutor App!"

if __name__ == "__main__":
    app.run(debug=True)
