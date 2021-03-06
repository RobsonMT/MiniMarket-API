from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.decorators import validate
from app.exceptions.generic_exception import (
    GenericKeyError,
    IdNotFound,
    MissingKeyError,
    UnauthorizedUser,
)
from app.models import AddressModel, CategoryModel, EstablishmentModel, UserModel
from app.services.populate_db import *
from app.services.populate_db import populate_categories_and_payments
from app.services.query_establishment_service import (
    filter_establishement,
    keys_address,
    keys_establishment,
    missing_keys_address,
    missing_keys_establishment,
)
from app.services.query_service import (
    create_svc,
    get_all_svc,
    get_by_id_svc,
    update_svc,
)


@jwt_required()
def post_establishment(user_id):

    try:
        get_by_id_svc(id=user_id, model=UserModel)
    except:
        return {"error": "The user_id entered is not valid"}, HTTPStatus.BAD_REQUEST

    data = request.get_json()

    if get_jwt_identity()["id"] != 1:
        return {
            "error": "You don't have access to this route because you are not admin"
        }, HTTPStatus.BAD_REQUEST

    try:

        if "address" not in data.keys():
            raise MissingKeyError
        address = data.pop("address")

        keys_address(data=address)
        keys_establishment(data=data)
        missing_keys_address(data=address)
        missing_keys_establishment(data=data)

        for key, value in data.items():

            if filter_establishement(EstablishmentModel, {key: value}):
                return {"error": f"{key} already exists"}, 409

        if filter_establishement(AddressModel, address):
            return {"error": "Address already exists"}, 409
        else:

            create_svc(AddressModel, address)
            data["user_id"] = user_id
            data["name"] = data["name"].title()
            data["address_id"] = filter_establishement(AddressModel, address)[0].id
            new_establishment = create_svc(EstablishmentModel, data)

            if len(CategoryModel.query.all()) == 0:
                populate_categories_and_payments()
        return jsonify(new_establishment), HTTPStatus.CREATED

    except GenericKeyError as err:
        return err.args[0], err.args[1]
    except MissingKeyError:
        return {
            "Error": "Missing establishment address",
            "address example": {
                "street": "street name",
                "number": "establishment number",
                "zip_code": "establishment zip code",
                "district": "establishment district",
            },
        }, HTTPStatus.BAD_REQUEST


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
