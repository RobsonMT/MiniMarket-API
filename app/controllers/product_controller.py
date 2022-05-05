from bdb import set_trace
from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_sqlalchemy import BaseQuery, Pagination
from psycopg2.errors import UniqueViolation
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.configs.database import db
from app.exceptions import FilterError, UnauthorizedUser
from app.exceptions.generic_exception import (
    MissingKeyError,
    UnauthorizedUser,
    WrongKeyError,
)
from app.models import ProductModel
from app.models.categories_model import CategoryModel
from app.models.establishment_model import EstablishmentModel
from app.models.product_categories import ProductCategory
from app.services import serialize_products_svc
from app.services.query_service import create_svc


@jwt_required()
def create_one_product() -> dict:
    user = get_jwt_identity()
    session: Session = db.session
    data = request.get_json()

    fields = [
        "name",
        "description",
        "sale_price",
        "cost_price",
        "unit_type",
        "url_img",
        "establieshment_id",
        "categories",
    ]

    expected = [
        "name",
        "sale_price",
        "cost_price",
        "unit_type",
        "establieshment_id",
        "categories",
    ]

    wrong_key = set(data.keys()).difference(fields)

    missing_key = set(expected).difference(data.keys())

    request_categories = data.get("categories")
    if request_categories:
        categories = data.pop("categories")

    establishment = EstablishmentModel.query.filter(
        and_(
            EstablishmentModel.id == data.get("establieshment_id"),
            EstablishmentModel.user_id == user["id"],
        ),
    ).one_or_none()

    try:
        if not establishment or user["id"] == 1:
            raise UnauthorizedUser
        if wrong_key:
            raise WrongKeyError

        product = create_svc(ProductModel, data)

    except UnauthorizedUser:
        session.rollback()
        return {
            "error": "you need to be the owner of the establishment to register a product."
        }, HTTPStatus.UNAUTHORIZED
    except MissingKeyError:
        session.rollback()
        return {
            "expected keys": list(expected),
            "missing key(s)": list(missing_key),
        }, HTTPStatus.BAD_REQUEST
    except WrongKeyError:
        session.rollback()
        return {
            "accepted keys": list(fields),
            "wrong key(s)": list(wrong_key),
        }, HTTPStatus.BAD_REQUEST
    except IntegrityError as exc:
        isinstance(exc.orig, UniqueViolation)
        session.rollback()
        return {"error": "product already exits!"}, HTTPStatus.CONFLICT
    else:
        for name in categories:
            category = CategoryModel.query.filter_by(name=name).first()
            new_pc_data = {"product_id": product.id, "category_id": category.id}

            create_svc(ProductCategory, new_pc_data)

        response = serialize_products_svc([product])

        return jsonify(response), HTTPStatus.OK
    finally:
        session.close()


@jwt_required()
def get_all_products(establishment_id: int) -> dict:
    user = get_jwt_identity()
    session: Session = db.session

    base_query: BaseQuery = session.query(ProductModel)
    page = request.args.get("page", type=int)
    per_page = request.args.get("per_page", type=int)

    establishment = EstablishmentModel.query.filter(
        and_(
            EstablishmentModel.id == establishment_id,
            EstablishmentModel.user_id == user["id"],
        ),
    ).one_or_none()

    if page and per_page:
        products: Pagination = (
            base_query.order_by(ProductModel.id)
            .paginate(page=page, per_page=per_page)
            .items
        )

    else:
        products = ProductModel.query.filter_by(
            establieshment_id=establishment_id
        ).all()

    try:
        if not establishment and user["id"] != 1:
            raise UnauthorizedUser

        if not products:
            raise FilterError

        response = serialize_products_svc(products)

        return {"data": response}, HTTPStatus.OK
    except UnauthorizedUser:
        return {
            "error": "you need to be the owner of the establishment to register a product."
        }, HTTPStatus.UNAUTHORIZED
    except FilterError:
        return {"data": "You don't have any products"}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_product_by_id(establishment_id: int, product_id: int) -> dict:
    # def get_product_by_id(product_id: int) -> dict:
    user = get_jwt_identity()
    # result = get_by_id_svc(model=ProductModel, id=product_id)

    establishment = EstablishmentModel.query.filter(
        and_(
            EstablishmentModel.id == establishment_id,
            EstablishmentModel.user_id == user["id"],
        )
    ).one_or_none()

    product = ProductModel.query.filter(
        and_(
            ProductModel.establieshment_id == establishment_id,
            ProductModel.id == product_id,
        )
    ).all()

    # return jsonify(result), HTTPStatus.OK
    try:
        if not establishment:
            raise UnauthorizedUser
        if not product:
            raise FilterError
        response = serialize_products_svc(product)
        return jsonify({"data": response}), HTTPStatus.OK
    except UnauthorizedUser:
        return {
            "error": "you need to be the owner of the establishment to register a product."
        }, HTTPStatus.UNAUTHORIZED
    except FilterError:
        return {"error": "product not found"}, HTTPStatus.NOT_FOUND


@jwt_required()
def get_product_by_query_parameters(establishment_id: int) -> dict:
    user = get_jwt_identity()
    args = request.args

    category = args.get("category", default="", type=str)

    establishment = EstablishmentModel.query.filter(
        and_(
            EstablishmentModel.id == establishment_id,
            EstablishmentModel.user_id == user["id"],
        ),
    ).one_or_none()

    products = ProductModel.query.filter(
        ProductModel.establieshment_id == establishment_id,
    ).all()

    output = []

    for product in products:
        for c in product.categories:
            if category.title() in c.name:
                product_data = {
                    "id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "sale_price": product.sale_price,
                    "cost_price": product.cost_price,
                    "unit_type": product.unit_type,
                    "url_img": product.url_img,
                    "establieshment_id": product.establieshment_id,
                    "categories": [c.name for c in product.categories],
                }

                output.append(product_data)

    try:
        if not establishment and user["id"] != 1:
            raise UnauthorizedUser

        if not output:
            raise FilterError

    except UnauthorizedUser:
        return {
            "error": "you need to be the owner of the establishment to register a product."
        }, HTTPStatus.UNAUTHORIZED
    except FilterError:
        return {"error": "product not found"}, HTTPStatus.NOT_FOUND
    else:
        return jsonify(output), HTTPStatus.OK


@jwt_required()
def patch_product(establishment_id: int, product_id: int) -> dict:
    session: Session = db.session
    user = get_jwt_identity()
    data = request.get_json()

    fields = [
        "name",
        "description",
        "sale_price",
        "cost_price",
        "unit_type",
        "url_img",
        "establieshment_id",
        "categories",
    ]

    wrong_key = set(data.keys()).difference(fields)

    request_categories = data.get("categories")
    if request_categories:
        data.pop("categories")

        all_categories_name = [c.name for c in CategoryModel.query.all()]

        for name in request_categories:
            if not name in all_categories_name:
                return {"error": "category type not acepted"}, HTTPStatus.NOT_FOUND

    establishment = EstablishmentModel.query.filter(
        and_(
            EstablishmentModel.id == establishment_id,
            EstablishmentModel.user_id == user["id"],
        )
    ).one_or_none()

    product: ProductModel = ProductModel.query.filter(
        and_(
            ProductModel.id == product_id,
            ProductModel.establieshment_id == establishment_id,
        )
    ).first()

    try:
        if not establishment and user["id"] != 1:
            raise UnauthorizedUser

        if wrong_key:
            raise WrongKeyError

        if not product:
            raise FilterError

        for key, value in data.items():
            setattr(product, key, value)
            session.commit()

        # categorias que serão mocadas
        products_categories_list = ProductCategory.query.filter(
            ProductCategory.product_id == product_id
        ).all()

        if request_categories:
            for product_category in products_categories_list:
                session.delete(product_category)
                session.commit()

            for name in request_categories:
                category = CategoryModel.query.filter_by(name=name).first()
                new_product_category = {
                    "product_id": product.id,
                    "category_id": category.id,
                }
                create_svc(ProductCategory, new_product_category)

        response = serialize_products_svc([product])

        return jsonify(response), HTTPStatus.OK

    except UnauthorizedUser:
        return {
            "error": "you need to be the owner of the establishment to register a product."
        }, HTTPStatus.UNAUTHORIZED
    except WrongKeyError:
        return {
            "accepted keys": list(fields),
            "wrong key(s)": list(wrong_key),
        }, HTTPStatus.BAD_REQUEST
    except FilterError:
        return {"error": "product not found."}, HTTPStatus.NOT_FOUND
