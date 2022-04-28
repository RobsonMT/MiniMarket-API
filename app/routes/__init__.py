from flask import Blueprint, Flask

from app.routes.client_blueprint import bp_clients
from app.routes.establishment_blueprint import bp_establishment
from app.routes.product_blueprint import bp_products
from app.routes.sale_blueprint import bp_sales
from app.routes.user_blueprint import bp_users
from app.routes.auth_blueprint import bp_auth

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_auth)
    bp_api.register_blueprint(bp_users)
    bp_api.register_blueprint(bp_products)
    bp_api.register_blueprint(bp_clients)
    bp_api.register_blueprint(bp_establishment)
    bp_api.register_blueprint(bp_sales)

    app.register_blueprint(bp_api)
