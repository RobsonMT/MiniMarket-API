from flask import Blueprint
from app.controllers.product_controller import create_one_product

bp_products = Blueprint("db_products", __name__, url_prefix="/products")

bp_products.post("")(create_one_product)