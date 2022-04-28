from flask import Flask

from app import routes
from app.configs import database, migrations, jwt_auth


def create_app():
    app = Flask(__name__)

    database.init_app(app)
    migrations.init_app(app)
    jwt_auth.init_app(app)
    routes.init_app(app)

    return app
