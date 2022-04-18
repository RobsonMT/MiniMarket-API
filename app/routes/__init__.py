from  flask import Flask
from app.routes.user_blueprint import bp_users
from app.routes.establishment_blueprint import bp_establishments
from app.routes.product_blueprint import bp_products
from app.routes.client_blueprint import bp_clients

def init_app(app: Flask):
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_establishments)
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_clients)