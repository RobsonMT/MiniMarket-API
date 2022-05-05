INSERT INTO users
    ("name", email, "password", avatar, contact)
VALUES
    (
        'Merdolino Mendonça',
        'merdolino@email.com',
        '123456', 
        'https://cdn.pixabay.com/photo/2016/08/18/11/00/man-1602633_960_720.png',
        '33 93562-3647'
    ),(
        'Inocêncio Coitadinho',
        'inocencio@email.com',
        '123456', 
        'https://cdn.pixabay.com/photo/2016/08/18/11/00/man-1602633_960_720.png',
        '33 935890-3647'
    );
INSERT INTO adresses
    (street, "number", zip_code, district)
VALUES
    (
        'Rua Adrualdo Monte Alto', 
        234,
        '35010-29', 
        'Goval'
     ),(
        'Rua Meia Volta', 
        777,
        '35980-29', 
        'Itu'
     );

INSERT INTO establishments
    ("name", cnpj, address_id, contact, url_logo, "user_id")
VALUES
    (
        'Merdolinos Frutas',
        '34.956.947/0001-28',
        1,
        '33 3172-3654',
        'https://cdn.pixabay.com/photo/2017/03/16/21/18/logo-2150297_960_720.png',
        1
    ),(
        'Mercadinho do Bairro',
        '34.956.437/0001-28',
        2,
        '33 3302-3954',
        'https://cdn.pixabay.com/photo/2017/03/16/21/18/logo-2150297_960_720.png',
        2
    );

INSERT INTO clients
    ("name", avatar, contact, estabilishment_id, pay_day)
VALUES
    (
        'Maria das Graças',
        'https://cdn.pixabay.com/photo/2021/05/10/08/00/woman-6242836_960_720.png',
        '33 98846-5704',
        1,
        null
    ),(
        'Ricardo Pereira',
        'https://cdn.pixabay.com/photo/2021/05/10/08/00/woman-6242836_960_720.png',
        '33 98846-5374',
        2,
        null
    );








INSERT INTO categories
    ("name", url_img)
VALUES
    (
        'Frutas',
        'https://cdn.pixabay.com/photo/2019/08/01/19/48/fruit-4378178_960_720.png'
    );

INSERT INTO payments
    (form_of_payment)
VALUES
    ('À Vista'),
    ('Crediário');
    
INSERT INTO products
    ("name", description, sale_price, cost_price, unit_type, url_img, category_id, establishment_id)
VALUES
    (
        'Banana',
        'Banana caturra',
        5.00,
        3.00,
        'kl', 
        'https://cdn.pixabay.com/photo/2014/12/21/23/39/bananas-575773_960_720.png', 
        (SELECT id FROM categories WHERE id = 1),
        (SELECT id FROM establishments WHERE id = 1)
    ),(
        'Maçã',
        'Maçã Argentina',
        3.49,
        3.10,
        'kl', 
        'https://cdn.pixabay.com/photo/2014/12/21/23/39/bananas-575773_960_720.png', 
        (SELECT id FROM categories WHERE id = 1),
        (SELECT id FROM establishments WHERE id = 2)
    );

INSERT INTO sales
    ("date", paid_date, client_id, payment_id, sale_total, remain_to_pay)
VALUES
    (
        TO_DATE('17/12/2015', 'DD/MM/YYYY'),
        null,
        (SELECT id FROM clients WHERE id = 1),
        (SELECT id FROM payments WHERE id = 2),
        8.49,
        null
    ),(
        TO_DATE('17/12/2022', 'DD/MM/YYYY'),
        TO_DATE('17/12/2022', 'DD/MM/YYYY'),
        (SELECT id FROM clients WHERE id = 2),
        (SELECT id FROM payments WHERE id = 1),
        5.00,
        null
    );

INSERT INTO product_categories
    (product_id, category_id)
VALUES
    (
        (SELECT id FROM products WHERE id = 1),
        (SELECT id FROM categories WHERE id = 1)
    ),(
        (SELECT id FROM products WHERE id = 1),
        (SELECT id FROM categories WHERE id = 2)
    );

INSERT INTO sales_products
    (sale_id, product_id)
VALUES
    (
        (SELECT id FROM sales WHERE id = 1),
        (SELECT id FROM products WHERE id = 1)
    ),(
        (SELECT id FROM sales WHERE id = 1),
        (SELECT id FROM products WHERE id = 1)
    ),(
        (SELECT id FROM sales WHERE id = 1),
        (SELECT id FROM products WHERE id = 1)
    );