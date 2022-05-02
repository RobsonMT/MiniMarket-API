from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError

from app.exceptions import UnauthorizedUser, FilterError
from app.models import SaleModel, AddressModel
from app.services import query_service


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

from ipdb import set_trace

def get_sales(client_id):
    
    data = {"client_id": client_id, "paid_date": None}
    try:
        sales_found = query_service.filter_svc(AddressModel, data)
        return jsonify(sales_found), HTTPStatus.OK
    except FilterError:
        return {"message": "No sales on client"}, HTTPStatus.NOT_FOUND


@jwt_required()
def get_sale_by_id(id):
    try:
        sale = query_service.get_by_id_svc(SaleModel, id)
    except:
        return {"error": "Sale (ID) doesn't exist"}, HTTPStatus.BAD_REQUEST
    return jsonify(sale), 200
