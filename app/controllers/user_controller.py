from http import HTTPStatus

from flask import jsonify

from app.decorators import validate_fields
from app.exceptions.generic_exception import IdNotFound, TableEmpty
from app.models.user_model import UserModel
from app.services.query_service import get_all_svc, get_by_id_svc


@validate_fields(UserModel)
def post_user():
    return "ROTA create USER"
    """
    CRIAR USUARIO
    => verificar se o usuario e o id 1
        . rota protegida
    """


def patch_user(id):
    return "ROTA path USER"

    """
    ATUALIZAR USUARIO
    rota protegida
    => verificar se o usuario e o id 1
    """


def get_all():
    try:
        users = get_all_svc(Model=UserModel)
    except TableEmpty as err:
        return err.args[0], err.args[1]
    return jsonify(users), HTTPStatus.OK

    """"
    RETORNA TODOS OS USUARIOS
    => verificar se o usuario e o id 1
        rota protegida
    """


def get_by_id(id):
    try:
        user = get_by_id_svc(model=UserModel, id=id)
    except IdNotFound as err:
        return err.args[0], err.args[1]
    return jsonify(user), HTTPStatus.OK

    """
    RETORNA UM USUÁRIO EXCECIFICO
    rota protegida
    => verificar se o usuario e o id 1
        rota protegida
    """
