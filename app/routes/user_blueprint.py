from flask import Blueprint
from app.controllers.user_controller import create_one_user

bp_users = Blueprint("db_users", __name__, url_prefix="/users")

bp_users.post("")(create_one_user)