def create_one_product():
    return "ROTA create product"


def patch_product(id):
    """
    rota protegida: verifica se o dono da aplicação tem o producte com base no id
    arquivar producte
    """
    return "Rota patch product"


def get_all_products():
    """
    rota protegida: busca todos os productes desse vendedor
    """
    return "get_all_products"


def get_one_product(id):
    """
    rota protegida: busca um producte especifico.
    verifica se o producte pertence a esse comerciante
    """
    return "get one product"
