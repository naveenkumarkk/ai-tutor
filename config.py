import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

    # MySQL database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql://root:12345@localhost/study-beam'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Google OAuth configuration
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

    # Microsoft OAuth configuration
    MS_CLIENT_ID = os.getenv('MS_CLIENT_ID')
    MS_CLIENT_SECRET = os.getenv('MS_CLIENT_SECRET')
    MS_AUTHORITY = "https://login.microsoftonline.com/common"
    MS_SCOPE = ["User.Read", "Tasks.ReadWrite", "Calendars.ReadWrite"]
    MS_REDIRECT_URI = "http://localhost:5000/ms/callback"  # Your redirect URI after MS auth
