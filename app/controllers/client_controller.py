def create_one_client():
    return "ROTA create CLIENT"

def patch_client():
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

def get_one_client():
    """
    rota protegida: busca um cliente especifico.
    verifica se o cliente pertence a esse comerciante
    """
    try:
        return "get one client"
    except ErrorFound as err:
        return str(err)



