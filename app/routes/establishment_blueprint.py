from flask import Blueprint
from app.controllers.establishment_controller import create_one_establishment

bp_establishments = Blueprint("db_establishments", __name__, url_prefix="/establishments")

bp_establishments.post("")(create_one_establishment)