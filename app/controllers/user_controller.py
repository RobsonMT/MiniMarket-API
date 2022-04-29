from app.decorators import validate_fields
from app.exceptions import IdNotFound, TableEmpty
from app.models.user_model import UserModel
from app.services.query_service import get_by_id_svc, update_svc, get_all_svc
from app.services.query_user_service import validate_user_data_svc
from flask import jsonify, request
from http import HTTPStatus


@validate_fields(UserModel)
def post_user():
    return "ROTA create USER"
    """
    CRIAR USUARIO
    => verificar se o usuario e o id 1
        . rota protegida
    """

@validate_fields(UserModel)
def patch_user(id):
    data = request.get_json()
    try:
        validate_keys = validate_user_data_svc(data, UserModel)
        update_user = update_svc(UserModel, id, validate_keys)

        return jsonify(update_user), 200
    except IdNotFound as err:
        return err.args[0], err.args[1]



  

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
    RETORNA UM USUÁRIO EXPECIFICO
    rota protegida
    => verificar se o usuario e o id 1
        rota protegida
    """
