from flask import Blueprint

from app.controllers import user_controller

bp_users = Blueprint("bp_users", __name__, url_prefix="/users")

bp_users.get("")(user_controller.get_all)
bp_users.get("<int:id>")(user_controller.get_by_id)
bp_users.patch("<int:id>")(user_controller.patch_user)
bp_users.post("")(user_controller.post_user)
