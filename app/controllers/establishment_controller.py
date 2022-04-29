from flask import request, jsonify
from app.services.query_service import create_svc, update_svc,get_by_id_svc
from app.decorators import validate
from app.models import AddressModel, EstablishmentModel, UserModel
from http import HTTPStatus
from app.exceptions.generic_exception import IdNotFound
from app.services.query_service import get_by_id_svc
from flask_jwt_extended import (
    create_access_token, 
    get_jwt_identity,
    jwt_required
    )

def post_establishment():
    data = request.get_json()
    address = data.pop('address')
    
    try:
        create_svc(AddressModel, address)
        
        data['address_id'] = AddressModel.query.filter_by(zip_code=address.get('zip_code')).first().id
        
        new_establishment = create_svc(EstablishmentModel, data)

        return new_establishment
    except:
        ...

@jwt_required()
@validate(EstablishmentModel)
def patch_establishment(id):
    data = request.get_json()

    try:
        update = update_svc(EstablishmentModel, id, data)
        return jsonify(update)
   
    except IdNotFound as err:
        return err.args[0], err.args[1]


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
