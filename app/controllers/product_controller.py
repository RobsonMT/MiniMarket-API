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
from app.services.query_service import get_by_id_svc


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
def patch_product(id: int) -> dict:
    """
    rota protegida: verifica se o dono da aplicação tem o producte com base no id
    arquivar producte
    """
    return "Rota patch product"

