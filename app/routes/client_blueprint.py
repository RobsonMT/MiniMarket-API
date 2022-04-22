from flask import Blueprint
from app.controllers import client_controller

bp_clients = Blueprint("db_clients", __name__, url_prefix="/clients")

bp_clients.get("")(client_controller.create_one_client)