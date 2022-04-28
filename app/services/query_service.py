from http import HTTPStatus

from app.exceptions import IdNotFound, TableEmpty


def get_all_svc(Model, order=None):

    response = (
        Model.query.order_by(order.desc()).all() if order != None else Model.query.all()
    )

    if len(response) == 0:
        raise TableEmpty

    return response


def get_by_id_svc(model, id):
    response = model.query.get(id)
    if not response:
        raise IdNotFound({"error": f"id {id} not found"}, HTTPStatus.BAD_REQUEST)
    return response


def filter_svc(model, field, search):
    ...


def create_svc(model, data):
    ...


def update_svc(session, model, id, data):

    response = get_by_id_svc(model, id)
    
    for key, value in data.items():
        setattr(response, key, value)

    session.add(response)
    session.commit()

    return response

def delete_svc(model, id):
    ...
