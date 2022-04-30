import re

from flask import jsonify

from app.exceptions import (
    CellphoneAlrealyExists,
    EmailAlrealyExists,
    InvalidCellphone,
    WrongKeyError,
)

from .query_service import get_all_svc

"""
Query para criar categorias mockadas e os produtos iniciais da plataforma, associados ao usuário
Essa query provavalmente 
"""


def create_categories_and_products():
    ...


def validate_user_data_svc(data, Model):
    valid_keys = ["name", "email", "contact", "password", "avatar", "is_activate"]
    data_keys = data.keys()

    for key in data_keys:
        if key not in valid_keys:
            raise WrongKeyError

    if (
        "contact" in data_keys
        and not re.search("\(..\).....\-....$", data["contact"])
        or len(data["contact"]) != 14
    ):
        raise InvalidCellphone

    all_users = get_all_svc(Model)
    serialize_users = [
        {"contact": user.contact, "email": user.email} for user in all_users
    ]
    emails = [user["email"] for user in serialize_users]
    cellphones = [user["contact"] for user in serialize_users]

    if "email" in data_keys and data["email"] in emails:
        raise EmailAlrealyExists
    if "email" in data_keys and data["contact"] in cellphones:
        raise CellphoneAlrealyExists

    return data
