from http import HTTPStatus
<<<<<<< HEAD
from app.exceptions.generic_exception import IdNotFound, UnauthorizedUser
from app.services.query_service import get_by_id_svc
from flask_jwt_extended import get_jwt_identity, jwt_required

@jwt_required
=======

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.decorators import validate
from app.exceptions.generic_exception import IdNotFound
from app.models import AddressModel, EstablishmentModel, UserModel
from app.services.query_service import create_svc, get_by_id_svc, update_svc


>>>>>>> 0fef58b0214f3da8b55d2012c333b3fa4383980e
def post_establishment():
    data = request.get_json()
    address = data.pop("address")

    try:
        create_svc(AddressModel, address)

        data["address_id"] = (
            AddressModel.query.filter_by(zip_code=address.get("zip_code")).first().id
        )

        new_establishment = create_svc(EstablishmentModel, data)

        return new_establishment, HTTPStatus.CREATED
    except:
        ...


@jwt_required()
@validate(EstablishmentModel)
def patch_establishment(id):
    user_id = get_jwt_identity()["id"]
    data = request.get_json()

    try:
        search_establishment = get_by_id_svc(model=EstablishmentModel, id=id)
        if user_id != 1 and search_establishment.user_id !=user_id:
            raise UnauthorizedUser

        update = update_svc(EstablishmentModel, id, data)
        return jsonify(update)

    except IdNotFound as err:
        return err.args[0], err.args[1]

    except UnauthorizedUser:
        return {"Error": "Unauthorized user" }, HTTPStatus.UNAUTHORIZED


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
def get_establishment_by_name(name):
    name = name.title()
    user_email = get_jwt_identity()["email"]
    establishments = (
        UserModel.query.filter(UserModel.email.like(user_email)).one().establishment
    )
    try:
        establishment = EstablishmentModel.query.filter(
            EstablishmentModel.name.like(name)
        ).one()
    except:
        return {"error": f"Name {name} not found"}, HTTPStatus.BAD_REQUEST
    establishments = [place for place in establishments if place == establishment]
    if establishments == []:
        return {"error": "You do not own this establishment"}, HTTPStatus.BAD_REQUEST
    return {"establishment": establishments[0]}, HTTPStatus.OK
