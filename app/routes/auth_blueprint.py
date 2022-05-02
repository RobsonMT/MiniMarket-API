from flask import Blueprint

from app.controllers import auth_controller

bp_auth = Blueprint("bp_auth", __name__)

bp_auth.post("/signin")(auth_controller.signin)
bp_auth.post("/signup")(auth_controller.signup)
bp_auth.get("/users")(auth_controller.get_user)
