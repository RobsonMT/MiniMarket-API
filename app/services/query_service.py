from http import HTTPStatus

from flask import current_app, jsonify

from app.exceptions import IdNotFound, TableEmpty


def get_all_svc(Model, order=None):

    response = (
        Model.query.order_by(order.desc()).all() if order != None else Model.query.all()
    )

    if len(response) == 0:
        raise TableEmpty({"error": "No registered user"}, HTTPStatus.BAD_REQUEST)

    return response


def get_by_id_svc(model, id):
    response = model.query.get(id)
    if not response:
        raise IdNotFound({"error": f"id {id} not found"}, HTTPStatus.BAD_REQUEST)
    return response


def filter_svc(model, field, search):
    ...


from ipdb import set_trace


def create_svc(Model, data):

    session = current_app.db.session
    new_data = Model(**data)
    session.add(new_data)
    session.commit()

    return jsonify(new_data)


def update_svc(model, id, data):
    response = get_by_id_svc(model, id)
    session = current_app.db.session

    for key, value in data.items():
        setattr(response, key, value)

    if not response:
        raise IdNotFound({"error": f"id {id} not found"}, HTTPStatus.BAD_REQUEST)

    session.add(response)
    session.commit()

    return response


def delete_svc(model, id):
    ...
