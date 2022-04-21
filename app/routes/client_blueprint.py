from flask import Blueprint
from app.controllers import client_controller

bp_clients = Blueprint("db_clients", __name__, url_prefix="/clients")