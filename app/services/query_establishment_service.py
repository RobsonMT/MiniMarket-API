from http import HTTPStatus

from app.exceptions.generic_exception import GenericKeyError
from flask import current_app

def keys_establishment(data):
    fields = ["name", "cnpj", "contact", "url_logo"]

    wrong_key = set(data.keys()).difference(fields)

    if wrong_key:
        raise GenericKeyError(
            {
                "accepted keys": list(fields),
                "wrong key(s)": list(wrong_key),
            },
            HTTPStatus.BAD_REQUEST,
        )


def keys_address(data):
    fields = ["street", "number", "zip_code", "district"]

    wrong_key = set(data.keys()).difference(fields)

    if wrong_key:
        raise GenericKeyError(
            {
                "accepted keys": list(fields),
                "wrong key(s)": list(wrong_key),
            },
            HTTPStatus.BAD_REQUEST,
        )


def missing_keys_establishment(data):
    expected = ["name", "cnpj", "contact", "url_logo"]
    missing_key = set(expected).difference(data.keys())
    if missing_key:
        raise GenericKeyError(
            {
                "expected keys": list(expected),
                "missing key(s)": list(missing_key),
            },
            HTTPStatus.BAD_REQUEST,
        )


def missing_keys_address(data):
    expected = ["street", "number", "zip_code", "district"]
    missing_key = set(expected).difference(data.keys())
    if missing_key:
        raise GenericKeyError(
            {
                "expected keys": list(expected),
                "missing key(s)": list(missing_key),
            },
            HTTPStatus.BAD_REQUEST,
        )
def filter_establishement(Model, fields):
    session = current_app.db.session

    founds = session.query(Model).filter_by(**fields).all()

    if founds:
        return founds
    return None