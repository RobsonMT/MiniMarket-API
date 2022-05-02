from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.exceptions.generic_exception import IdNotFound
from app.models import ClientModel
from app.models.establishment_model import EstablishmentModel
from app.models.user_model import UserModel
from app.services.query_service import create_svc, get_by_id_svc


@jwt_required()
def post_client():

    data = request.get_json()

    try:
        new_client = create_svc(ClientModel, data)

        return new_client, HTTPStatus.CREATED
    except:
        ...


@jwt_required()
def patch_client(id):
    """
    rota protegida: verifica se o dono da aplicação tem o cliente com base no id
    arquivar cliente
    """
    return "Rota patch client"


@jwt_required()
def get_all_clients(establishment_id):

    user_email = get_jwt_identity()["email"]
    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishments
    )

    try:
        establishment = get_by_id_svc(model=EstablishmentModel, id=establishment_id)
    except IdNotFound as err:
        return err.args[0], err.args[1]

    establishments = [place for place in establishments if place == establishment]
    if establishments == []:
        return {"error": "You do not own this establishment"}, HTTPStatus.BAD_REQUEST
    if establishments[0].clients == []:
        return {
            "error": "This establishment does not have any customers"
        }, HTTPStatus.BAD_REQUEST
    return jsonify(establishments[0].clients), HTTPStatus.OK


@jwt_required()
def get_one_client(establishment_id, client_id):
    user_email = get_jwt_identity()["email"]
    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishments
    )
    try:
        establishment = get_by_id_svc(model=EstablishmentModel, id=establishment_id)
    except IdNotFound as err:
        return err.args[0], err.args[1]

    establishments = [place for place in establishments if place == establishment]
    if establishments == []:
        return {"error": "You do not own this establishment"}, HTTPStatus.BAD_REQUEST
    if establishments[0].clients == []:
        return {
            "error": "This establishment does not have any customers"
        }, HTTPStatus.BAD_REQUEST
    try:
        client = get_by_id_svc(model=ClientModel, id=client_id)
    except IdNotFound as err:
        return err.args[0], err.args[1]

    for user in establishments[0].clients:
        if user == client:
            return jsonify(client), HTTPStatus.OK

    return {
        "error": "This client is not from the requested establishment"
    }, HTTPStatus.BAD_REQUEST
