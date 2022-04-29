from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.decorators import validate_fields, validate
from app.exceptions import  IdNotFound,  TableEmpty
from app.models.user_model import UserModel
from app.services.query_service import get_all_svc, get_by_id_svc, update_svc
from app.services.query_user_service import validate_user_data_svc


@jwt_required()
@validate(UserModel)
def patch_user(id):
    data = request.get_json()
    try:
        validate_keys = validate_user_data_svc(data, UserModel)
        update_user = update_svc(UserModel, id, validate_keys)

        return jsonify(update_user), 200
    except IdNotFound as err:
        return err.args[0], err.args[1]
 
@jwt_required()
def get_all():
    try:
        users = get_all_svc(Model=UserModel)
    except TableEmpty as err:
        return err.args[0], err.args[1]
    return jsonify(users), HTTPStatus.OK


@jwt_required()
def get_by_id(id):
    try:
        user = get_by_id_svc(model=UserModel, id=id)
    except IdNotFound as err:
        return err.args[0], err.args[1]
    return jsonify(user), HTTPStatus.OK
