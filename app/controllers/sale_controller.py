from http import HTTPStatus

from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.decorators import validate_sale_fields
from app.exceptions import IdNotFound, UnauthorizedUser
from app.exceptions.generic_exception import WrongKeyError
from app.models import ClientModel, SaleModel
from app.models.establishment_model import EstablishmentModel
from app.models.product_model import ProductModel
from app.models.sale_product_model import SaleProductModel
from app.services.query_service import create_svc, get_by_id_svc, update_svc


@jwt_required()
@validate_sale_fields(SaleModel)
def post_sale() -> dict:
    user = get_jwt_identity()
    data = request.get_json()
    request_products = data.pop("products")

    establishments_of_user = EstablishmentModel.query.filter(
        EstablishmentModel.user_id == user["id"],
    ).all()

    product_id_database = [p.id for p in ProductModel.query.all()]

    have_product_id_invalid = bool(
        set(request_products).difference(product_id_database)
    )

    try:
        for establishment in establishments_of_user:
            for client in establishment.clients:
                if client.id != data.get("client_id") or user["id"] == 1:
                    raise UnauthorizedUser

        if have_product_id_invalid:
            raise TypeError

        sale: SaleModel = create_svc(SaleModel, data)

        for id in request_products:
            new_sale_product = {"sale_id": sale.id, "product_id": id}
            create_svc(SaleProductModel, new_sale_product)

        return (
            {
                "id": sale.id,
                "date": sale.date,
                "paid_date": sale.paid_date,
                "client_id": sale.client_id,
                "payment_id": sale.payment_id,
                "sale_total": sale.sale_total,
                "remain_to_pay": sale.remain_to_pay,
                "payment_method": sale.payment_method.form_of_payment,
            },
            HTTPStatus.OK,
        )
    except TypeError:
        return {"error": "product of request id not acepted"}, HTTPStatus.NOT_ACCEPTABLE
    except UnauthorizedUser:
        return {
            "error": "the customer must belong to an establishment you already own"
        }, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_sale_by_id(establishment_id: int, id: int) -> dict:

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
def patch_sale(client_id: int, sale_id: int) -> dict:
    user = get_jwt_identity()
    data = request.get_json()

    fields = ["paid_date", "remain_to_pay"]

    wrong_key = set(data.keys()).difference(fields)

    establishments_of_user = EstablishmentModel.query.filter(
        EstablishmentModel.user_id == user["id"],
    ).all()

    try:
        if wrong_key:
            raise WrongKeyError

        for establishment in establishments_of_user:
            for client in establishment.clients:
                if client.id != client_id and user["id"] != 1:
                    raise UnauthorizedUser

        sale = update_svc(SaleModel, sale_id, data)

        return {
            "id": sale.id,
            "date": sale.date,
            "paid_date": sale.paid_date,
            "client_id": sale.client_id,
            "sale_total": sale.sale_total,
            "remain_to_pay": sale.remain_to_pay,
            "payment_method": sale.payment_method.form_of_payment,
        }, HTTPStatus.OK
    except WrongKeyError:
        return {
            "accepted keys": list(fields),
            "wrong key(s)": list(wrong_key),
        }, HTTPStatus.BAD_REQUEST
    except IdNotFound as err:
        return err.args[0], err.args[1]
    except UnauthorizedUser:
        return {
            "error": "the customer must belong to an establishment you already own"
        }, HTTPStatus.UNAUTHORIZED


@jwt_required()
def get_sales(establishment_id: int) -> dict:
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
