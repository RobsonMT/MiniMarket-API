from http import HTTPStatus

from app.exceptions import TableEmpty
from app.models import ProductModel, EstablishmentModel
from app.services.query_service import get_by_id_svc


def create_one_product():
    return "ROTA create product"


def patch_product(id):
    """
    rota protegida: verifica se o dono da aplicação tem o producte com base no id
    arquivar producte
    """
    return "Rota patch product"


def get_all_products(establishment_id):
    products = (
        get_by_id_svc(EstablishmentModel,establishment_id).products
    )
    if products == []:
        return {"error": "You don't have any products"}, HTTPStatus.BAD_REQUEST
    return {"products": products}, HTTPStatus.OK


def get_one_product(id):
    """
    rota protegida: busca um producte especifico.
    verifica se o producte pertence a esse comerciante
    """
    return "get one product"
