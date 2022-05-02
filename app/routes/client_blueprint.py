from flask import Blueprint

from app.controllers import client_controller

bp_clients = Blueprint("bp_clients", __name__)

bp_clients.post("/client")(client_controller.post_client)
bp_clients.get("/establishment/<int:establishment_id>/client")(
    client_controller.get_all_clients
)
bp_clients.get("/establishment/<int:establishment_id>/client/<int:client_id>")(
    client_controller.get_one_client
)
bp_clients.patch("/client/<int:id>")(client_controller.patch_client)
