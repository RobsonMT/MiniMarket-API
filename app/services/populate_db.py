<<<<<<< Updated upstream
from flask import current_app
from ipdb import set_trace

from app.models import (CategoryModel, PaymentModel, ProductCategory,
                        ProductModel)
from app.services import query_product_service, query_service


def populate_categories_and_payments():
    categories = [
    {
        "name": "Hortifruti",
        "url_img":"https://lorensonline.com.br/wp-content/uploads/2019/06/Lorens-Crescimento-do-Hortifruti-no-Brasil-legumes-sortidos-2.jpg"
    },{
        "name": "Produtos de limpeza",
        "url_img":"https://cglimpeza.com.br/wp-content/uploads/2018/12/2019-01-itens-indispensaveis-no-estoque-de-produtos-para-limpeza-1.jpg"
    },{
        "name": "Higiene e perfumaria",
        "url_img":"https://site.abcfarma.org.br/wp-content/uploads/2019/05/loja-de-cosmeticos-virtual-como-montar-1.jpg"
    },{
        "name": "Congelados",
        "url_img":"https://boaforma.abril.com.br/wp-content/uploads/sites/2/2018/07/thinkstockphotos-626104514.jpg"
    },{
        "name": "Carnes",
        "url_img":"https://www.saboravida.com.br/wp-content/uploads/2019/12/veja-como-preparar-diferentes-cortes-de-carnes-800x445.jpg"
    },{
        "name": "Latas e conservas",
        "url_img":"https://www.bonduelle.com.br/images/produtos/latas-conservas.png"
    },{
        "name": "Farinhas e grãos",
        "url_img":"https://nutritotal.com.br/publico-geral/wp-content/uploads/sites/2/2019/09/shutterstock_272086718-1.jpg"
    },{
        "name": "Frios",
        "url_img":"https://www.sabornamesa.com.br/media/k2/items/cache/01db144526716df630e705de85c35be7_XL.jpg"
    },{
        "name": "Legumes",
        "url_img":"https://s2.glbimg.com/wpd84CZmDM9Wzn2sWdLoQdHoB6s=/0x0:750x500/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2020/h/I/6O16OJRB2sUMIDqtxlmQ/alimentos-crus.jpg"
    },{
        "name": "Bebidas",
        "url_img":"https://www.galaxcms.com.br/imgs_crud_comum/1801/Bebidas-acucaradas-incluindo--20190711142328.jpg"
    },{
        "name": "Padaria",
        "url_img":"https://730370.smushcdn.com/1861587/wp-content/uploads/2021/09/balcao-de-padaria-1024x576.jpg?lossy=1&strip=1&webp=1"
    },{
        "name": "açougue",
        "url_img":"https://blog.atau.com.br/wp-content/uploads/2018/08/Dicas-para-atrair-mais-clientes-para-o-seu-acougue-atau-1900x1069.jpg"
    },{
        "name": "Energéticos",
        "url_img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRezTO51dI9vlvGVC_l8AYRjNRSc7dVxEN80Q&usqp=CAU"
    },{
        "name": "Biscoitos e Chocolates",
        "url_img":"https://www.marolacomcarambola.com.br/wp-content/uploads/2016/10/receita-de-biscoitos-confeitados-com-chocolate-2.jpg"
    }
]
    for category in categories:
        query_service.create_svc(CategoryModel, category)
    payments =  [{
        "form_of_payment": "A vista",
    },{
        "form_of_payment": "Crediário",
    } ] 
    for payment in payments:
        query_service.create_svc(PaymentModel, payment)
     
def populate_products(establieshment_id):
    session = current_app.db.session

    products = [
        {
            "name": "Tomate Grape Dueto Frutano 300g",
            "description": "Tomate Grape Dueto Frutano 300g",
            "sale_price": 6.99,
            "cost_price": 4.03,
            "unit_type": "un",
            "url_img": "https://zonasul.vtexassets.com/arquivos/ids/3045025/VF4qT-qqCUAAAAAAAAHLtQ.jpg?v=637792744791970000",
            "categories": ["Hortifruti"],
            "establieshment_id": establieshment_id
        },{
            "name": "Amac C Uau 1l Lav Frescor",
            "description": "Amac C Uau 1l Lav Frescor",
            "sale_price": 13.97,
            "cost_price": 8.03,
            "unit_type": "un",
            "url_img": "https://s3.amazonaws.com/produtos.vipcommerce.com.br/250x250/faa51489-f135-4e57-999a-dfa27f9abff7.jpg",
            "categories": ["Produtos de limpeza"],
            "establieshment_id": establieshment_id
        },{
            "name": "Chocolate Meio Amargo Com Amêndoas Garoto Talento Pacote 85g",
            "description": "Chocolate Meio Amargo Com Amêndoas Garoto Talento Pacote 85g",
            "sale_price": 6.99,
            "cost_price": 3.07,
            "unit_type": "un",
            "url_img": "https://images-americanas.b2w.io/produtos/2811326856/imagens/chocolate-garoto-talento-meio-amargo-amendoas-com-90g/2811326901_1_xlarge.jpg",
            "categories": ["Biscoitos e Chocolates"],
            "establieshment_id": establieshment_id
        }
    ]
    
    for product in products:
        categories = product.pop('categories')
        
        product_id = query_service.create_svc(ProductModel, product).id

        for category in categories:
            category_id = session.query(CategoryModel).filter_by(name=category).first().id
            data = {"product_id":product_id, "category_id": category_id}
            
            query_service.create_svc(ProductCategory, data)
                
=======
from app.models import CategoryModel
from app.services import query_service


def populate_categories():
    categories = [
        {
            "name": "Hortifruti",
            "url_img": "https://lorensonline.com.br/wp-content/uploads/2019/06/Lorens-Crescimento-do-Hortifruti-no-Brasil-legumes-sortidos-2.jpg",
        },
        {
            "name": "Produtos de limpeza",
            "url_img": "https://cglimpeza.com.br/wp-content/uploads/2018/12/2019-01-itens-indispensaveis-no-estoque-de-produtos-para-limpeza-1.jpg",
        },
        {
            "name": "Higiene e perfumaria",
            "url_img": "https://site.abcfarma.org.br/wp-content/uploads/2019/05/loja-de-cosmeticos-virtual-como-montar-1.jpg",
        },
        {
            "name": "Congelados",
            "url_img": "https://boaforma.abril.com.br/wp-content/uploads/sites/2/2018/07/thinkstockphotos-626104514.jpg",
        },
        {
            "name": "Carnes",
            "url_img": "https://www.saboravida.com.br/wp-content/uploads/2019/12/veja-como-preparar-diferentes-cortes-de-carnes-800x445.jpg",
        },
        {
            "name": "Latas e conservas",
            "url_img": "https://www.bonduelle.com.br/images/produtos/latas-conservas.png",
        },
        {
            "name": "Farinhas e grãos",
            "url_img": "https://nutritotal.com.br/publico-geral/wp-content/uploads/sites/2/2019/09/shutterstock_272086718-1.jpg",
        },
        {
            "name": "Frios",
            "url_img": "https://www.sabornamesa.com.br/media/k2/items/cache/01db144526716df630e705de85c35be7_XL.jpg",
        },
        {
            "name": "Legumes",
            "url_img": "https://s2.glbimg.com/wpd84CZmDM9Wzn2sWdLoQdHoB6s=/0x0:750x500/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2020/h/I/6O16OJRB2sUMIDqtxlmQ/alimentos-crus.jpg",
        },
        {
            "name": "Bebidas",
            "url_img": "https://www.galaxcms.com.br/imgs_crud_comum/1801/Bebidas-acucaradas-incluindo--20190711142328.jpg",
        },
        {
            "name": "Padaria",
            "url_img": "https://730370.smushcdn.com/1861587/wp-content/uploads/2021/09/balcao-de-padaria-1024x576.jpg?lossy=1&strip=1&webp=1",
        },
        {
            "name": "açougue",
            "url_img": "https://blog.atau.com.br/wp-content/uploads/2018/08/Dicas-para-atrair-mais-clientes-para-o-seu-acougue-atau-1900x1069.jpg",
        },
        {
            "name": "Energéticos",
            "url_img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRezTO51dI9vlvGVC_l8AYRjNRSc7dVxEN80Q&usqp=CAU",
        },
        {
            "name": "Biscoitos e Chocolates",
            "url_img": "https://www.marolacomcarambola.com.br/wp-content/uploads/2016/10/receita-de-biscoitos-confeitados-com-chocolate-2.jpg",
        },
    ]
    for category in categories:
        query_service.create_svc(CategoryModel, category)
>>>>>>> Stashed changes
