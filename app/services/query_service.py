from exceptions import *

def get_all_svc(model):...

def get_by_id_svc(model, id):
    
    response = model.query.get(id)
    
    if not response:
        raise IdNotFound({"error": f"id {id} not found"}, HTTPStatus.BAD_REQUEST)
    
    return response

def filter_svc(model, field):...

def create_svc(model, data):...

def update_svc(model, id ,data):...

def delete_svc(model, data):...
