from flask import Blueprint
from app.controllers import product_controller

bp_products = Blueprint("bp_products", __name__, url_prefix="/products")

bp_products.get("")(product_controller.get_all_products)
bp_products.get("<int:id>")(product_controller.get_one_product)
bp_products.post("")(product_controller.create_one_product)
bp_products.patch("<int:id>")(product_controller.patch_product)
