from bdb import set_trace
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.configs.database import db
from app.decorators import validate_sale_fields
from app.exceptions import (FilterError, IdNotFound, UnauthorizedUser,
                            establishment_exception)
from app.models import ClientModel, SaleModel
from app.models.establishment_model import EstablishmentModel
from app.models.product_model import ProductModel
from app.models.sale_product_model import SaleProductModel
from app.services import query_service
from app.services.query_service import create_svc, get_by_id_svc


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
def get_sale_by_id(establishment_id, id):

    try:
        establishment = get_by_id_svc(EstablishmentModel, establishment_id)
        if (
            get_jwt_identity()["id"] != 1
            and get_jwt_identity()["id"] != establishment.user_id
        ):
            return {
                "error": "You do not own the establishment referring to the informed customer"
            }, HTTPStatus.BAD_REQUEST
    except IdNotFound as err:
        return err.args[0], err.args[1]

    try:
        sale = get_by_id_svc(SaleModel, id)
    except:
        return {
            "error": f"The sale with the id {id} did not exist"
        }, HTTPStatus.BAD_REQUEST

    if get_by_id_svc(ClientModel, sale.client_id).establishment_id != establishment_id:
        return {
            "error": "The informed establishment does not hold the past sale"
        }, HTTPStatus.BAD_REQUEST

    return {
        "id": sale.id,
        "date": sale.date,
        "paid_date": sale.paid_date,
        "client_id": sale.client_id,
        "payment_id": sale.payment_id,
        "sale_total": sale.sale_total,
        "remain_to_pay": sale.remain_to_pay,
        "payment_method": sale.payment_method.form_of_payment,
        "products": [
            get_by_id_svc(ProductModel, product.product_id).name
            for product in SaleProductModel.query.filter_by(sale_id=sale.id).all()
        ],
    }, HTTPStatus.OK


@jwt_required()
def patch_sale(id):
    data = request.get_json()

    try:
        return query_service.update_svc(SaleModel, id, data)
    except IdNotFound as err:
        return err.args[0], err.args[1]


@jwt_required()
def get_sales(establishment_id):

    try:
        establishment = get_by_id_svc(EstablishmentModel, establishment_id)
        if (
            get_jwt_identity()["id"] != 1
            and get_jwt_identity()["id"] != establishment.user_id
        ):
            return {
                "error": "You do not own the establishment referring to the informed customer"
            }, HTTPStatus.BAD_REQUEST
    except IdNotFound as err:
        return err.args[0], err.args[1]

    clients = ClientModel.query.filter_by(establishment_id=establishment_id).all()

    if clients == []:
        return {
            "error": "The informed establishment dont have customers"
        }, HTTPStatus.BAD_REQUEST

    serialized_clients = []

    for client in clients:
        serialized_clients.append(
            {
                "id": client.id,
                "name": client.name,
                "sales": [
                    {
                        "id": sale.id,
                        "date": sale.date,
                        "paid_date": sale.paid_date,
                        "client_id": sale.client_id,
                        "payment_id": sale.payment_id,
                        "sale_total": sale.sale_total,
                        "remain_to_pay": sale.remain_to_pay,
                        "payment_method": sale.payment_method.form_of_payment,
                        "products": [
                            get_by_id_svc(ProductModel, product.product_id).name
                            for product in SaleProductModel.query.filter_by(
                                sale_id=sale.id
                            ).all()
                        ],
                    }
                    for sale in SaleModel.query.filter_by(client_id=client.id).all()
                ],
            }
        )

    return {"clients": serialized_clients}, HTTPStatus.OK

    # for sale in sales:
    #     serialized_sales.append({
    #     "id": sale.id,
    #     "date": sale.date,
    #     "paid_date": sale.paid_date,
    #     "client_id": sale.client_id,
    #     "payment_id": sale.payment_id,
    #     "sale_total": sale.sale_total,
    #     "remain_to_pay": sale.remain_to_pay,
    #     "payment_method": sale.payment_method.form_of_payment,
    #     "products" : [
    #     get_by_id_svc(ProductModel, product.product_id).name
    #     for product in SaleProductModel.query.filter_by(sale_id=sale.id).all()
    # ]
    # })

    # return {"sales": serialized_sales}, HTTPStatus.OK
