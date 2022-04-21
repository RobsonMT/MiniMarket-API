from flask import request, jsonify
from http import HTTPStatus
from app.services import query_service
from app.models.sale_model import SaleModel

def post_sale():
    obj_body = request.get_json()
    try:
        query_service.create_svc(SaleModel, obj_body)
    except:
        return {"error": "sale already registered"}, HTTPStatus.CONFLICT
    return "ROTA post (create) SALE"

def patch_sale(obj_id):
    obj_body = request.get_json()
    try:
        query_service.update_svc(SaleModel, obj_id, obj_body)
    except:
        return {"error": "key doesn't exist"}, HTTPStatus.BAD_REQUEST
    return "ROTA patch SALE"

def get_sales():
    query_service.get_all_svc(SaleModel)
    return "ROTA get (all) SALES"

def get_sale_by_id(obj_id):
    try:
        query_service.get_by_id_svc(SaleModel, obj_id)
    except:
        return {"error": "id doesn't exist"}, HTTPStatus.BAD_REQUEST
    return "ROTA get_sale_by_id SALE"