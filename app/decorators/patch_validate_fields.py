from functools import wraps
from http import HTTPStatus
from typing import Callable

from flask import request

from app.exceptions import WrongKeyError


def validate(Model):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            fields = {
                c.name
                for c in Model.__table__.c
                if c.name != "id" 
            }
            wrong_key = set(data.keys()).difference(fields)
            try:
                if wrong_key:
                    raise WrongKeyError(
                        {
                            "accepted keys": list(fields),
                            "wrong key(s)": list(wrong_key),
                        }
                    )
                return func(*args, **kwargs)
            except (WrongKeyError) as e:
                return e.args[0], HTTPStatus.BAD_REQUEST

        return wrapper

    return decorator
