from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.decorators import validate
from app.exceptions import (
  IdNotFound,
  TableEmpty,
  UnauthorizedUser,
)
from app.models.user_model import UserModel
from app.services.query_service import ( get_all_svc, get_by_id_svc,
                                        update_svc)


@jwt_required()
@validate(UserModel)
def patch_user(id):
    token_user_id = get_jwt_identity()["id"]
    data = request.get_json()
    try:
        if token_user_id != id and token_user_id != 1:
            raise UnauthorizedUser
        update_user = update_svc(UserModel, id, data)

        return jsonify(update_user), 200

    except IdNotFound as err:
        return err.args[0], err.args[1]

    except UnauthorizedUser:
        return {"Error": "Unauthorized user"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def deactivatte_or_activate_user(id):
    token_user_id = get_jwt_identity()["id"]

    try:
        if token_user_id != 1:
            raise UnauthorizedUser

        user = get_by_id_svc(UserModel, id)
        user.is_activate = not user.is_activate
        update_svc(UserModel, id, user.__dict__)

        if user.is_activate == False:
            return {"Error": "Deactivated user"}, 200
        return {"message": "Activate user"}, 200

    except UnauthorizedUser:
        return {"Error": "Unauthorized user"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_all_users():
    token_user_id = get_jwt_identity()["id"]
    try:
        if token_user_id != 1:
            raise UnauthorizedUser

        users = get_all_svc(Model=UserModel)
        return jsonify(users), HTTPStatus.OK

    except TableEmpty as err:
        return err.args[0], err.args[1]
    except UnauthorizedUser:
        return {"Error": "Unauthorized user"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_by_id(id):
    token_user_id = get_jwt_identity()["id"]
    try:
        if token_user_id != 1:
            raise UnauthorizedUser
        user = get_by_id_svc(model=UserModel, id=id)

        return jsonify(user), HTTPStatus.OK

    except IdNotFound as err:
        return err.args[0], err.args[1]
    except UnauthorizedUser:
        return {"Error": "Unauthorized user"}, HTTPStatus.UNAUTHORIZED
