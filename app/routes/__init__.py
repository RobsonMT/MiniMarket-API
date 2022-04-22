from flask import Flask, Blueprint
from app.routes.user_blueprint import bp_users
from app.routes.product_blueprint import bp_products
from app.routes.client_blueprint import bp_clients

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

def init_app(app: Flask):
    app.register_blueprint(bp_api)
    
bp_api.register_blueprint(bp_users)
bp_api.register_blueprint(bp_clients)
bp_api.register_blueprint(bp_products)
