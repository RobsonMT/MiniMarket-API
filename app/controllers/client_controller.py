from http import HTTPStatus

from flask import request

from app.models import ClientModel
from app.services.query_service import create_svc


def post_client():

    data = request.get_json()

    try:

        new_client = create_svc(ClientModel, data)

        return new_client, HTTPStatus.CREATED
    except:
        ...


def patch_client(id):
    """
    rota protegida: verifica se o dono da aplicação tem o cliente com base no id
    arquivar cliente
    """
    return "Rota patch client"


def get_all_clients():
    """
    rota protegida: busca todos os clientes desse vendedor
    """
    return "get_all_clients"


def get_one_client(id):
    """
    rota protegida: busca um cliente especifico.
    verifica se o cliente pertence a esse comerciante
    """
    return "get one client"
