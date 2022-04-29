from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)
from app.exceptions.generic_exception import IdNotFound
from app.models.establishment_model import EstablishmentModel
from app.models.user_model import UserModel
from app.services.query_service import get_by_id_svc


def patch_establishment(id):
    """
    rota protegida: verifica se o dono da aplicação tem o establishment com base no id
    arquivar establishmente
    """
    return "Rota patch establishment"


@jwt_required()
def get_all_establishments():
    user_email = get_jwt_identity()["email"]
    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishment
    )
    if establishments == []:
        return {"error": "You don't have any establishment"}, HTTPStatus.BAD_REQUEST
    return {"establishments": establishments}, HTTPStatus.OK


@jwt_required()
def get_one_establishment(id):
    user_email = get_jwt_identity()["email"]
    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishment
    )
    try:
        establishment = get_by_id_svc(model=EstablishmentModel, id=id)
    except IdNotFound as err:
        return err.args[0], err.args[1]
    establishments = [place for place in establishments if place == establishment]
    if establishments == []:
        return {"error": "You do not own this establishment"}, HTTPStatus.BAD_REQUEST
    return {"establishment": establishments[0]}, HTTPStatus.OK


@jwt_required()
def get_establishment_by_name():
    data = request.get_json()
    if len(data) != 1:
        return {"error": "Invalid number of fields"}, HTTPStatus.BAD_REQUEST
    try:
        name = data["name"]
    except:
        return {"error": "The field passed is invalid"}, HTTPStatus.BAD_REQUEST
    user_email = get_jwt_identity()["email"]
    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishment
    )
    try:
        establishment = EstablishmentModel.query.filter(
            EstablishmentModel.name.like(name)
        ).one()
    except:
        return {"error": f"Name {data['name']} not found"}, HTTPStatus.BAD_REQUEST
    establishments = [place for place in establishments if place == establishment]
    if establishments == []:
        return {"error": "You do not own this establishment"}, HTTPStatus.BAD_REQUEST
    return {"establishment": establishments[0]}, HTTPStatus.OK
