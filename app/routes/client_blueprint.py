from flask import Blueprint

from app.controllers import client_controller

bp_clients = Blueprint("bp_clients", __name__)

bp_clients.post("/clients")(client_controller.post_client)
bp_clients.get("/establishments/<int:establishment_id>/clients")(
    client_controller.get_all_clients
)
bp_clients.get("/establishments/<int:establishment_id>/clients/<int:client_id>")(
    client_controller.get_one_client
)
bp_clients.patch("/establishments/<int:establishment_id>/clients/<int:client_id>")(
    client_controller.patch_client
)
