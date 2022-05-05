from flask import Blueprint

from app.controllers import product_controller

bp_products = Blueprint("bp_products", __name__)


bp_products.post("/products")(product_controller.create_one_product)
bp_products.get("/establishments/<int:establishment_id>/products")(
    product_controller.get_all_products
)
bp_products.get("/establishments/<int:establishment_id>/products/<int:product_id>")(
    product_controller.get_product_by_id
)
bp_products.patch("/establishments/<int:establishment_id>/products/<int:product_id>")(
    product_controller.patch_product
)
bp_products.get("/establishments/<int:establishment_id>/products/query")(
    product_controller.get_product_by_query_parameters
)

bp_products.get("/categories")(product_controller.get_all_categories)
