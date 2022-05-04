import re
from http import HTTPStatus


def regex_checker(regex, string):
    if re.fullmatch(regex, string) == None:
        return "deu ruim"
    else:
        return "string"
