from flask import Blueprint

from app.controllers import sale_controller

bp_sales = Blueprint("bp_sales", __name__)


bp_sales.post("/sales")(sale_controller.post_sale)
bp_sales.get("/sales/establishment/<int:establishment_id>")(sale_controller.get_sales)
bp_sales.get("/establishment/<int:establishment_id>/sales/<int:id>")(
    sale_controller.get_sale_by_id
)
bp_sales.patch("clients/<int:client_id>/sales/<int:sale_id>")(
    sale_controller.patch_sale
)
