def serialize_products_svc(products):
    output = []

    for product in products:

        product_data = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "sale_price": product.sale_price,
            "cost_price": product.cost_price,
            "unit_type": product.unit_type,
            "url_img": product.url_img,
            "establishment_id": product.establishment_id,
            "categories": [c.name for c in product.categories],
        }

        output.append(product_data)

    return output
