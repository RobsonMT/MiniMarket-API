from bdb import set_trace
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from app.decorators import validate_sale_fields

from app.exceptions import FilterError, IdNotFound, UnauthorizedUser
from app.models import SaleModel, sale_model
from app.models.product_model import ProductModel
from app.models.sale_product_model import SaleProductModel
from app.services import query_service
from sqlalchemy.orm import Session
from app.configs.database import db
from app.services.query_service import create_svc


@jwt_required()
@validate_sale_fields(SaleModel)
def post_sale() -> dict:
    data = request.get_json()
    # session: Session = db.session
    request_products = data.pop("products")
    user = get_jwt_identity()

    product_id_list = [p.id for p in ProductModel.query.all()]

    #  retorna a diferença dos ids invalidos
    requet_id_invalid = bool(set(request_products).difference(product_id_list))

    if requet_id_invalid:
        return {"error": "product of request error"}

    # try:
    sale: SaleModel = create_svc(SaleModel, data)
    for id in request_products:
        new_sale_product = {"sale_id": sale.id, "product_id": id}
        create_svc(SaleProductModel, new_sale_product)

    return jsonify(data), HTTPStatus.OK
    # except:
    #     ...


@jwt_required()
def get_sale_by_id(id):
    try:
        sale = query_service.get_by_id_svc(SaleModel, id)
        print(sale)
    except:
        return {"error": "Sale (ID) doesn't exist"}, HTTPStatus.BAD_REQUEST

    return {
        "id": sale.id,
        "date": sale.date,
        "paid_date": sale.paid_date,
        "client_id": sale.client_id,
        "payment_id": sale.payment_id,
        "sale_total": sale.sale_total,
        "remain_to_pay": sale.remain_to_pay,
        "payment_method": sale.payment_method.form_of_payment,
    }, 200


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
