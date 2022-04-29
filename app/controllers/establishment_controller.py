from app.services.query_service import update_svc
from flask import jsonify, request, current_app
from app.models import EstablishmentModel
from app.decorators import validate
from app.exceptions  import IdNotFound

@validate(EstablishmentModel)
def patch_establishment(id):
    data = request.get_json()

    try:
        update = update_svc(EstablishmentModel, id, data)
        return jsonify(update)
   
    except IdNotFound as err:
        return err.args[0], err.args[1]

def get_all_establishments():
    """
    rota protegida: busca todos os establishments desse vendedor
    """
    return "get_all_establishments"


def get_one_establishment(id):
    """
    rota protegida: busca um establishment especifico.
    verifica se o establishmente pertence a esse comerciante
    """
    return "get one establishment"

