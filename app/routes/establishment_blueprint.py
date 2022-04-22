from flask import Blueprint
from app.controllers import establishment_controller

bp_establishments = Blueprint("db_establishments", __name__, url_prefix="/establishments")
