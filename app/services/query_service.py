from http import HTTPStatus

from flask import current_app, jsonify
from sqlalchemy import and_, or_, create_engine
from sqlalchemy.orm import sessionmaker
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

from ipdb import set_trace

def filter_svc(Model, data):
    
    #session = current_app.db.session
    session_maker = sessionmaker(bind=current_app)
    session = session_maker()
    
    filters = []
    set_trace()
    for col in data:
        sqlalchemybinaryexpression = (getattr(Model, col) == data[col])
        filters.append(sqlalchemybinaryexpression)
    set_trace()  
    #query = Model.__table__.select().where(and_(*filters))
    #query= session.query(Model).filter(**data)
    # query = session.query(Model)
    # for attr,value in data.iteritems():
    #     query = query.filter( getattr(Model,attr)==value )
    
    # q = session.query(Model)
    # for attr, value in data.items():
    #     q = q.filter(getattr(Model, attr).like("%%%s%%" % value))
    
    query = session.query(Model).filter_by(name = 'JulioPereira').first()
    
    set_trace()
    return ""

def create_svc(Model, data):

    session = current_app.db.session
    new_data = Model(**data)
    session.add(new_data)
    session.commit()

    return jsonify(new_data)


def update_svc(session, model, id, data):

    response = get_by_id_svc(model, id)

    for key, value in data.items():
        setattr(response, key, value)

    session.add(response)
    session.commit()

    return response


def delete_svc(model, id):
    ...
