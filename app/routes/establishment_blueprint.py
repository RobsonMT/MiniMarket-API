from flask import Blueprint

from app.controllers import establishment_controller

bp_establishment = Blueprint("bp_establishment", __name__, url_prefix="/establishments")

bp_establishment.post("")(establishment_controller.post_establishment)
bp_establishment.get("")(establishment_controller.get_all_establishments)
bp_establishment.get("<int:id>")(establishment_controller.get_one_establishment)
bp_establishment.get("/name/<name>")(establishment_controller.get_establishment_by_name)
bp_establishment.patch("<int:id>")(establishment_controller.patch_establishment)
