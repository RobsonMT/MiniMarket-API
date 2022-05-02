from http import HTTPStatus
from itertools import product
from turtle import update

from flask import jsonify, request, session
from flask_jwt_extended import jwt_required, get_jwt_identity
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.exceptions.generic_exception import IdNotFound, UnauthorizedUser
from app.models import ProductModel
from app.models.categories_model import CategoryModel
from app.models.establishment_model import EstablishmentModel
from app.models.product_categories import ProductCategory
from app.services.query_service import create_svc, filter_svc, get_by_id_svc, update_svc


def create_one_product() -> dict:
    data = request.get_json()
    session: Session = db.session

    categories = data.pop("categories")

    try:
        product = create_svc(ProductModel, data)
    except IntegrityError as exc:
        isinstance(exc.orig, UniqueViolation)
        session.rollback()
        return {"error": "product already exits!"}, HTTPStatus.CONFLICT
    else:
        for name in categories:
            category = CategoryModel.query.filter_by(name=name).first()
            new_pc_data = {"product_id": product.id, "category_id": category.id}

            create_svc(ProductCategory, new_pc_data)

        data.update({"categories": categories})

        return jsonify(data), HTTPStatus.OK
    finally:
        session.close()


@jwt_required()
def get_all_products(establishment_id: int) -> dict:
    products = ProductModel.query.filter_by(establieshment_id=establishment_id).all()
    if products == []:
        return {"error": "You don't have any products"}, HTTPStatus.BAD_REQUEST
    return {"products": products}, HTTPStatus.OK


@jwt_required()
def get_product_by_id(establishment_id: int, product_id: int) -> dict:
    ...


@jwt_required()
def patch_product(establishment_id: int, product_id: int) -> dict:
    data = request.get_json()
    session: Session = db.session
    query = session.query(ProductModel)

    try:
        products = jsonify(query.filter_by(establieshment_id=establishment_id, id=product_id).first())
        val_prod = products.get_json()

        if val_prod:
            for key, value in val_prod.items():
                if key=='establieshment_id':
                    establishment_product_id = value
        else:
            raise IdNotFound

        if establishment_product_id == establishment_id:
            update = update_svc(ProductModel, product_id, data)

            return jsonify(update), 200

    except IdNotFound:
        return jsonify(error = "Product ID doesn't exists."), 400
    except IntegrityError:
        return jsonify(error = "Product ID already exists."), 400


