from flask import Blueprint
from app.controllers.sale_controller import create_one_sale, update_one_sale, delete_one_sale

bp_sales = Blueprint("db_sales", __name__, url_prefix="/sales")

bp_sales.post("")(create_one_sale)
bp_sales.patch("<int:sale_id>")(update_one_sale)
bp_sales.delete("<int:sale_id>")(delete_one_sale)