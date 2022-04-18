from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()


def init_app(app:Flask):

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS'))
    app.config['JSON_SORT_KEYS'] = bool(os.getenv('JSON_SORT_KEYS'))