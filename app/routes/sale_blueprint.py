from flask import Blueprint

from app.controllers import sale_controller

bp_sales = Blueprint("bp_sales", __name__, url_prefix="/sales")


bp_sales.post("")(sale_controller.post_sale)
bp_sales.get("client/<int:client_id>")(sale_controller.get_sales)
bp_sales.get("<int:id>")(sale_controller.get_sale_by_id)
bp_sales.patch("<int:id>")(sale_controller.patch_sale)
