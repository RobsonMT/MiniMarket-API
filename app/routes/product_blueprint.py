from flask import Blueprint
from app.controllers import product_controller

bp_products = Blueprint("db_products", __name__, url_prefix="/products")
