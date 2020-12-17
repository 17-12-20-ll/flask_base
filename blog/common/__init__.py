from flask import Flask
from blog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis


def create_app():
    current_app = Flask(__name__)
    current_app.config.from_object(Config)
    return current_app


db = SQLAlchemy(session_options={'autocommit': True})
app = create_app()

flask_redis = FlaskRedis()
