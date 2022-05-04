from datetime import timedelta
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions import AttributeTypeError, DisabledAccount, UnauthorizedUser, MissingKeyError, CellphoneAlreadyExists
from app.models import UserModel
from app.services.query_regex import regex_checker


def signin():
    data = request.get_json()
    session: Session = db.session
    user = session.query(UserModel).filter_by(email=data["email"]).first()

    try:
        if not user or not user.verify_password(data["password"]):
            raise AttributeTypeError

        if user.is_activate == False:
            raise DisabledAccount

        token = create_access_token(user, expires_delta=timedelta(minutes=100))
        return {"access_token": "{}".format(token)}, HTTPStatus.OK

    except DisabledAccount:
        return {"Error": "Your account is deactivated"}, HTTPStatus.UNAUTHORIZED

    except AttributeTypeError:
        return {"detail": "email and password missmatch"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def signup():
    obrigatory_keys = ["name", "email", "password", "contact"]
    user_id = get_jwt_identity()["id"]
    data = request.get_json()
    session: Session = db.session
    missing_keys = [key for key in obrigatory_keys if key not in data.keys()]
    try:
        if user_id != 1:
            raise UnauthorizedUser

        if len(missing_keys) > 0:
            raise MissingKeyError

        valid_if_cellphone_exists = UserModel.query.filter_by(contact=data["contact"]).all()
        if len(valid_if_cellphone_exists) >0:
            raise CellphoneAlreadyExists


        user = UserModel(**data)
        session.add(user)
        session.commit()

        data.pop("password")

        return jsonify(data), HTTPStatus.CREATED
    except UnauthorizedUser :
        return {"Error": "Unauthorized user. You need to be an admin to do it!"}, HTTPStatus.UNAUTHORIZED 
    except MissingKeyError:
        return jsonify({"obrigatory keys": obrigatory_keys, "optional_keys":['avatar'], "keys_missing":missing_keys}), HTTPStatus.BAD_REQUEST
    except CellphoneAlreadyExists:
        return {"Error":"The contact already exists"}, 409
    except IntegrityError:
        session.rollback()
        return {"error": "user already exists!"}, HTTPStatus.CONFLICT
        
    finally:
        session.close()


@jwt_required()
def get_user():
    user: UserModel = get_jwt_identity()

    return user, HTTPStatus.OK
