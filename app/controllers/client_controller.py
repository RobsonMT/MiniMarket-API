import json
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.decorators.patch_validate_fields import validate
from app.exceptions.generic_exception import IdNotFound, UnauthorizedUser
from app.models import ClientModel
from app.models.establishment_model import EstablishmentModel
from app.models.user_model import UserModel
from app.services.query_service import create_svc, get_by_id_svc, update_svc


@jwt_required()
def post_client():

    data = request.get_json()

    try:
        new_client = create_svc(ClientModel, data)

        return new_client, HTTPStatus.CREATED
    except:
        ...


@jwt_required()
@validate(ClientModel)
def patch_client(establishment_id, client_id):
    data = request.get_json()
    user_email = get_jwt_identity()["email"]
    if get_jwt_identity()["id"] == 1:
        try:
            update = update_svc(data=data, id=client_id, model=ClientModel)
            return jsonify(update)
        except IdNotFound as err:
            return err.args[0], err.args[1]
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
        update = update_svc(data=data, id=client_id, model=ClientModel)
    except IdNotFound as err:
        return err.args[0], err.args[1]

    return jsonify(update)


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
