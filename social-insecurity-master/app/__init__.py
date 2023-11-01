"""Provides the app package for the Social Insecurity application. The package contains the Flask app and all of the extensions and routes."""

from pathlib import Path
from typing import cast

from flask import Flask

from app.config import Config
from app.database import SQLite3

from werkzeug.security import check_password_hash

# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask_wtf.csrf import CSRFProtect

# Instantiate and configure the app
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the sqlite database extension
sqlite = SQLite3(app, schema="schema.sql")

# TODO: Handle login management better, maybe with flask_login?
# login = LoginManager(app)

# TODO: The passwords are stored in plaintext, this is not secure at all. I should probably use bcrypt or something
# bcrypt = Bcrypt(app)

def valid_login(username, password):
    """Checks if username-password combination is valid."""

    # Fetch the user record from the database
    user = sqlite.query("SELECT * FROM Users WHERE username=?", True, username)
    
    # If the user doesn't exist
    if not user:
        return False
    
    # If the user exists, check the hashed password
    return check_password_hash(user["password"], password)

# TODO: The CSRF protection is not working, I should probably fix that
# csrf = CSRFProtect(app)

# Create the instance and upload folder if they do not exist
with app.app_context():
    instance_path = Path(app.instance_path)
    if not instance_path.exists():
        instance_path.mkdir(parents=True, exist_ok=True)
    upload_path = instance_path / cast(str, app.config["UPLOADS_FOLDER_PATH"])
    if not upload_path.exists():
        upload_path.mkdir(parents=True, exist_ok=True)

# Import the routes after the app is configured
from app import routes  # noqa: E402,F401

app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
