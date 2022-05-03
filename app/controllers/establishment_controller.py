from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from psycopg2.errors import NotNullViolation
from sqlalchemy.exc import IntegrityError

from app.decorators import validate
from app.exceptions.generic_exception import IdNotFound, UnauthorizedUser
from app.models import AddressModel, EstablishmentModel, UserModel
from app.services.query_service import (
    create_svc,
    get_all_svc,
    get_by_id_svc,
    update_svc,
)


@jwt_required()
def post_establishment():
    data = request.get_json()
    data["user_id"] = get_jwt_identity()["id"]  # Pegar id da url (usar esse apenas para validar se é admin)
    data["name"] = data["name"].title()
    address = data.pop("address")  # validar todo o objeto, não apenas o numero

    data["address_id"] = AddressModel.query.filter_by(
        number=address.get("number")
    ).first()

    establishment = EstablishmentModel.query.filter_by(cnpj=data.get("cnpj")).first()

    if data["address_id"] != None:
        return {"error": "address already registered"}, HTTPStatus.BAD_REQUEST

    if establishment != None:
        return {"error": "establishment already registered"}, HTTPStatus.BAD_REQUEST

    try:
        create_svc(AddressModel, address)
    except IntegrityError as err:
        if type(err.orig) == NotNullViolation:
            return {"error": "Field(s) Missing on address"}, HTTPStatus.BAD_REQUEST

    data["address_id"] = (
        AddressModel.query.filter_by(number=address.get("number")).first().id
    )

    try:
        new_establishment = create_svc(EstablishmentModel, data)
    except IntegrityError as err:
        if type(err.orig) == NotNullViolation:
            return {
                "error": "Field(s) Missing on establishment"
            }, HTTPStatus.BAD_REQUEST

    return jsonify(new_establishment), HTTPStatus.CREATED


@jwt_required()
@validate(EstablishmentModel)
def patch_establishment(id):
    user_id = get_jwt_identity()["id"]
    data = request.get_json()

    try:
        search_establishment = get_by_id_svc(model=EstablishmentModel, id=id)
        if user_id != 1 and search_establishment.user_id != user_id:
            raise UnauthorizedUser

        update = update_svc(EstablishmentModel, id, data)
        return jsonify(update)

    except IdNotFound as err:
        return err.args[0], err.args[1]

    except UnauthorizedUser:
        return {"Error": "Unauthorized user"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_all_establishments():
    user_email = get_jwt_identity()["email"]
    user_id = get_jwt_identity()["id"]
    if user_id == 1:
        return jsonify(get_all_svc(EstablishmentModel))

    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishments
    )
    if establishments == []:
        return {"error": "You don't have any establishment"}, HTTPStatus.BAD_REQUEST

    serialized_establishments = []

    for estab in establishments:
        serialized_establishments.append(
            {
                "id": estab.id,
                "name": estab.name,
                "cnpj": estab.cnpj,
                "contact": estab.contact,
                "url_logo": estab.url_logo,
                "user_id": estab.user_id,
                "address": estab.address,
                "clients": [client.name for client in estab.clients],
            }
        )

    return {"establishments": serialized_establishments}, HTTPStatus.OK


@jwt_required()
def get_one_establishment(id):
    user_email = get_jwt_identity()["email"]
    user_id = get_jwt_identity()["id"]

    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishments
    )
    try:
        establishment = get_by_id_svc(model=EstablishmentModel, id=id)
        if user_id == 1:
            return jsonify(establishment)

    except IdNotFound as err:
        return err.args[0], err.args[1]

    establishments = [place for place in establishments if place == establishment]

    if establishments == []:
        return {"error": "You do not own this establishment"}, HTTPStatus.BAD_REQUEST
    return {
        "data": {
            "id": establishments[0].id,
            "name": establishments[0].name,
            "cnpj": establishments[0].cnpj,
            "contact": establishments[0].contact,
            "url_logo": establishments[0].url_logo,
            "user_id": establishments[0].user_id,
            "address": establishments[0].address,
            "clients": [client.name for client in establishments[0].clients],
        }
    }, HTTPStatus.OK


@jwt_required()
def get_establishment_by_name(name):
    name = name.title()
    user_email = get_jwt_identity()["email"]
    user_id = get_jwt_identity()["id"]

    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishments
    )
    try:
        establishment = EstablishmentModel.query.filter(
            EstablishmentModel.name.like(name)
        ).one()
        if user_id == 1:
            return {"establishment": establishment}, HTTPStatus.OK
    except:
        return {"error": f"Name {name} not found"}, HTTPStatus.BAD_REQUEST
    establishments = [place for place in establishments if place == establishment]
    if establishments == []:
        return {"error": "You do not own this establishment"}, HTTPStatus.BAD_REQUEST
    return {"establishment": establishments}, HTTPStatus.OK
