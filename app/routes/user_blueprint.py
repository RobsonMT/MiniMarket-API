from flask import Blueprint
from app.controllers import user_controller

bp_users = Blueprint("db_users", __name__, url_prefix="/users")