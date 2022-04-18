from flask import Blueprint
from app.controllers.client_controller import create_one_client

bp_clients = Blueprint("db_clients", __name__, url_prefix="/clients")

bp_clients.post("")(create_one_client)