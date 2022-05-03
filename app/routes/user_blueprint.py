from flask import Blueprint

from app.controllers import user_controller

bp_users = Blueprint("bp_users", __name__, url_prefix="/users")

bp_users.get("/all")(user_controller.get_all_users)
bp_users.get("<int:id>")(user_controller.get_by_id)
bp_users.patch("<int:id>")(user_controller.patch_user)
bp_users.patch("/changestate/<int:id>")(user_controller.deactivatte_or_activate_user)
