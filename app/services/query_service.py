
from app.exceptions import TableEmpty
from app.exceptions import IdNotFound

def get_all_svc(Model, order=None):
    all_things = Model.query.order_by(order.desc()).all() if order != None else Model.query.all()
    if len(all_things) == 0:
         raise TableEmpty
    return all_things

def get_by_id_svc(model, id):
    
    response = model.query.get(id)
    
    if not response:
        raise IdNotFound({"error": f"id {id} not found"}, HTTPStatus.BAD_REQUEST)
    
    return response

def filter_svc(model, field):...

def create_svc(model, data):...

def update_svc(model, id ,data):...

def delete_svc(model, data):...
