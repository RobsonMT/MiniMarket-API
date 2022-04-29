from flask import request
from app.services.query_service import create_svc
from app.models import AddressModel, EstablishmentModel

def post_establishment():
    data = request.get_json()
    address = data.pop('address')
    
    try:
        create_svc(AddressModel, address)
        
        data['address_id'] = AddressModel.query.filter_by(zip_code=address.get('zip_code')).first().id
        
        new_establishment = create_svc(EstablishmentModel, data)

        return new_establishment
    except:
        ...
        

def patch_establishment(id):
    """
    rota protegida: verifica se o dono da aplicação tem o establishment com base no id
    arquivar establishmente
    """
    return "Rota patch establishment"


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
