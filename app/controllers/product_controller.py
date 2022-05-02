from http import HTTPStatus

from flask import jsonify, request
from flask_jwt_extended import jwt_required
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models import ProductModel
from app.models.categories_model import CategoryModel
from app.models.product_categories import ProductCategory
from app.services.query_service import create_svc


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
def patch_product(id: int) -> dict:
    """
    rota protegida: verifica se o dono da aplicação tem o producte com base no id
    arquivar producte
    """
    return "Rota patch product"
