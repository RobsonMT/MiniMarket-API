
from http import HTTPStatus
from pydoc import cli

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError

from app.exceptions import FilterError, IdNotFound, UnauthorizedUser
from app.models import AddressModel, SaleModel, SaleProductModel, ClientModel, PaymentModel
from app.services import query_service
from functools import reduce


@jwt_required()
def post_sale():
    data = request.get_json()
    
    try:
        products = data.pop("products")
        data['sale_total'] = reduce(lambda x, y: x + y, [product['sale_price'] for product in products]) #sale_amount
        
        sale = query_service.create_svc(SaleModel, data)
        
        for product in products:
            data = {"product_id": product.id, "sale_id": sale.id}
            query_service.create_svc(SaleProductModel, data)
            
        new_data = {
            "id":sale.id,
            "date":sale.date,
            "paid_date": sale.paid_date,
            "client": query_service.filter_svc(ClientModel, {"id":sale.client_id}).name,
            "payment": query_service.filter_svc(PaymentModel, {"id":sale.payment_id}).form_of_payment,
            "sale_total": sale.sale_total,
            "remain_to_pay": sale.remain_to_pay
        }
        
        return new_data, 201
    
    except UnauthorizedUser:
        return {"error": "Unauthorized user."}, 401
    except IntegrityError:
        return {"error": "Sale (ID) already exists."}, 409
        
        query_service.create_svc(SaleModel, data)
        return jsonify(data), 201
    except UnauthorizedUser:
        return {"error": "Unauthorized user."}, 401
        
    # except IntegrityError:
    #     return {"error": "Sale (ID) already exists."}, 409


@jwt_required()
def patch_sale(id):
    data = request.get_json()

    try:
        return query_service.update_svc(SaleModel, id, data)
    except IdNotFound as err:
        return err.args[0], err.args[1]


@jwt_required()
def get_sales(client_id):
    
    data = {"client_id": client_id, "paid_date": None}
    try:
        sales_found = query_service.filter_svc(SaleModel, data)
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
