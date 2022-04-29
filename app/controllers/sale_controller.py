from http import HTTPStatus

from app.exceptions.generic_exception import IdNotFound, UnauthorizedUser
from app.models.sale_model import SaleModel
from app.services import query_service
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError


@jwt_required()
def post_sale():
    data = request.get_json()
    try:
            query_service.create_svc(SaleModel, data)
            return jsonify(data), 201
    except UnauthorizedUser:
        return {"error": "Unauthorized user."}, 401
    except IntegrityError:
        return {"error": "Sale (ID) already exists."}, 409

        


def patch_sale(id):
    # obj_body = request.get_json()
    # try:
    # query_service.update_svc(SaleModel, id, obj_body)
    # except:
    # return {"error": "key doesn't exist"}, HTTPStatus.BAD_REQUEST
    return "ROTA patch SALE"


def get_sales():
    query_service.get_all_svc(SaleModel)
    return "ROTA get (all) SALES"


def get_sale_by_id(id):
    try:
        query_service.get_by_id_svc(SaleModel, id)
    except:
        return {"error": "id doesn't exist"}, HTTPStatus.BAD_REQUEST
    return "ROTA get_sale_by_id SALE"
