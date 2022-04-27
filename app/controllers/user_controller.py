from app.decorators import validate_fields
from app.exceptions import IdNotFound, WrongKeyError, InvalidCellphone, CellphoneAlrealyExists, EmailAlrealyExists,TableEmpty
from app.models.user_model import UserModel
from app.services.query_service import get_by_id_svc, update_svc
from app.services.query_user_service import validate_user_data_svc
from flask import current_app, jsonify, request
from http import HTTPStatus


@validate_fields(UserModel)
def post_user():
    return "ROTA create USER"
    """
    CRIAR USUARIO
    => verificar se o usuario e o id 1
        . rota protegida
    """


def patch_user(id):
    data = request.get_json()
    session = current_app.db.session

    try:
        validate_keys =validate_user_data_svc(data, UserModel)
        update_user = update_svc(session, UserModel, id, validate_keys)
       
        return jsonify(update_user), 200

    except CellphoneAlrealyExists:
        return {"Error": f"The cellphone{data['contact']} alrealy exists in database"}, 409

    except EmailAlrealyExists:
        return {"Error": f"The email{data['email']} alrealy exists in database"}, 409

    except IdNotFound as err:
        return err.args[0], err.args[1]

    except InvalidCellphone:
        return {"error": "The contact needs to have the format(xx)xxxxx-xxxx"}, 400

    except TableEmpty:
        return {"Error": "The table is empty"}, 400

    except WrongKeyError:
        return {"Error": "Your request can have the keys name, email, contact, password, avatar e is_activate. But invalid keys went found"}, 400

def get_all():
    return "ROTA get USER"

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
