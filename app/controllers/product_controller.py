from http import HTTPStatus

from app.exceptions import TableEmpty
from app.models import ProductModel


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
        ProductModel.query.filter(ProductModel.establieshment_id.like(establishment_id)).all()
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
