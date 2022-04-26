from flask import Blueprint
from app.controllers import user_controller

bp_users = Blueprint("bp_users", __name__, url_prefix="/users")