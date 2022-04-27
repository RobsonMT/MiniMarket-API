from functools import wraps
from http import HTTPStatus
from typing import Callable

from flask import request

from app.exceptions import MissingKeyError, WrongKeyError


def validate_fields(Model):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()

            fields = [
                c.name
                for c in Model.__table__.c
                if c.name != "id" and c.default == None
            ]

            expected = [
                c.name
                for c in Model.__table__.c
                if c.nullable == False and c.name != "id"
            ]

            wrong_key = set(data.keys()).difference(fields)

            missing_key = set(expected).difference(data.keys())

            try:
                if wrong_key:
                    raise WrongKeyError(
                        {
                            "accepted keys": list(fields),
                            "wrong key(s)": list(wrong_key),
                        }
                    )
                if missing_key:
                    raise MissingKeyError(
                        {
                            "expected keys": list(expected),
                            "missing key(s)": list(missing_key),
                        }
                    )
                return func(*args, **kwargs)
            except (MissingKeyError, WrongKeyError) as e:
                return e.args[0], HTTPStatus.BAD_REQUEST

        return wrapper

    return decorator
