def create_one_establishment():
    return "ROTA create establishment"


def patch_establishment():
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


def get_one_establishment():
    """
    rota protegida: busca um establishment especifico.
    verifica se o establishmente pertence a esse comerciante
    """
    return "get one establishment"
