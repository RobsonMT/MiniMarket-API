from datetime import timedelta
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from ipdb import set_trace
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models import UserModel
from app.exceptions import DisabledAccount, AttributeTypeError


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

def signup():
    data = request.get_json()
    session: Session = db.session

    try:
        user = UserModel(**data)

        session.add(user)
        session.commit()

        data.pop("password")

        return jsonify(data), HTTPStatus.CREATED
    except IntegrityError:
        session.rollback()

        return {"error": "user already exists!"}, HTTPStatus.CONFLICT
    finally:
        session.close()


@jwt_required()
def get_user():
    user: UserModel = get_jwt_identity()


    return user, HTTPStatus.OK
