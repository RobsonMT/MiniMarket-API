from flask import Blueprint
from app.controllers import sale_controller

bp_sales = Blueprint("bp_sales", __name__, url_prefix="/sales")
