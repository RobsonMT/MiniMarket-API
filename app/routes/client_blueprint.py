from flask import Blueprint

from app.controllers import client_controller

bp_clients = Blueprint("bp_clients", __name__, url_prefix="/clients")

bp_clients.post("")(client_controller.post_client)
bp_clients.get("")(client_controller.get_all_clients)
bp_clients.get("<int:id>")(client_controller.get_one_client)
bp_clients.patch("<int:id>")(client_controller.patch_client)
