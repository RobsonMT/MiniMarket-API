from app.errors import ErrorFilter, ErrorId

def get_by_id(model, product_id):
    if "achou":
        return "achou!!"
    else:
        raise ErrorId("deu erro no id")
    
def get_product_filter(data):
    ...
    
