from http import HTTPStatus


class ErrorFound(Exception):
    def __init__(self, message=None, status_code=HTTPStatus.CONFLICT):

        if not message:
            self.message = "Error in values"
        else:
            self.message = message

        self.status_code = status_code


class IdNotFound(Exception):
    ...


class FilterError(Exception):
    ...


class TableEmpty(Exception):
    ...


class TableNotFound(Exception):
    ...


class AttributeTypeError(Exception):
    ...


class AttributeValueError(Exception):
    ...


class WrongKeyError(Exception):
    ...


class MissingKeyError(Exception):
    ...


class UnauthorizedUser(Exception):
    ...


class GenericKeyError(Exception):
    ...
