# MiniMarket-API

<br />
<div align="center">
  <a href="https://github.com/RobsonMT/MiniMarket-API">
    <img src="https://github.com/RobsonMT/MiniMarket-API/blob/feat/readme/assets/mmlogo.png?raw=true" alt="Logo" width="200" height="80">
  </a>

  <h3 align="center">MiniMarket API</h3>

  <p align="center">
    Uma API voltada para a gestão de pequenos comércios, focada em agilizar a organização dos pagamentos e a gestão dos clientes.
    <br />
    <br />
    <br />
    <a href="linkdovercel"><strong>Explore a aplicação no vercel.</strong></a>
    <br />
    <br />
    <a href="https://github.com/RobsonMT/MiniMarket-API/issues">Reportar um bug</a>
    ·
    <a href="https://github.com/RobsonMT/MiniMarket-API/issues">Sugerir uma funcionalidade</a>

  </p>
</div>

## Visão geral

  <ol>
    <li>
      <a href="#motivacao">Sobre o projeto</a>
      <ul>
        <li><a href="#tecnologias">Tecnologias</a></li>
      </ul>
    </li>
    <li>
      <a href="#instruções">Instruções</a>
      <ul>
        <li><a href="#instalação">Instalação</a></li>
      </ul>
    </li>
    <li>
    <a href="#rotas">Rotas</a>
      <ul>
        <li><a href="#AUTH">AUTH</a></li>
        <li><a href="#USERS">USERS</a></li>
        <li><a href="#CLIENTS">CLIENTS</a></li>
        <li><a href="#ESTABLISHMENT">ESTABLISHMENT</a></li>
        <li><a href="#PRODUCTS">PRODUCTS</a></li>
        <li><a href="#SALES">SALES</a></li>
      </ul>
    </li>
    <li><a href="#licenca">Licença</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>

## Tecnologias

Tecnologias utilizadas na construção dessa aplicação:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask SQLALchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Instruções

Este é um guia de como configurar e rodar a aplicação localmente, siga os seguintes passos:

### Instalação

Clone o repositório em sua máquina:
<br />

Via SSH:
<br />

`$ git clone git@github.com:RobsonMT/MiniMarket-API.git`
<br />

Via HTTPS:
<br />

`$ git clone https://github.com/RobsonMT/MiniMarket-API.git`
<br />

Crie um ambiente virtual (venv) para seus pacotes pelo comando:
<br />

`<filepath>$ python -m venv venv`
<br />

Ative o venv pelo comando:
<br />

`$ source venv/bin/activate`
<br />

Instale os pacotes contidos no `requirements.txt` através do comando:
<br />

`$ pip install -r requirements.txt`
<br />

## Rotas

<br />
<br />

## AUTH

Rotas de autenticação.

## POST signup

Cria um novo usuário.

`/api/signup`
<br />
Body (JSON):
<br />

```sh
{
  "name": "marcelo",
  "email": "marcelo@email.com",
  "password": "123456",
  "avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/User_font_awesome.svg/2048px-User_font_awesome.svg.png",
  "contact": "19 93588-3611"
}
```

## POST signin

Loga o usuário.

`/api/signin`
<br />
Body (JSON):
<br />

```sh
{"email": "marcelo@email.com",
"password": "123456"}
```

<br />
<br />

## USERS

Rotas de usuário.

## GET users

Retorna todos os usuários.

`/api/users`

## GET all users

Retorna todos os usuários.

`/api/users/all`

## GET user by id

Retorna todos os usuários.

`/api/users/<id>`

## PATCH user by id

Retorna todos os usuários.

`/api/users/<id>`

```sh
{
  "name": "Marcelo Menddes"
}
```

## PATCH change user state

Altera o estado ativo/inativo

`/api/users/changestate/<id>`

<br />
<br />

## CLIENTS

Rotas de clientes.

## GET all clients

Retorna todos os clientes do estabelecimento.

`api/establishment/<establishment_id>/client`

## GET client id by establishment id

Retorna UM cliente (id) do estabelecimento.

`/establishment/<establishment_id>/client/<client_id>`

## POST client

Cria um novo cliente.

`/api/users/api/client

```sh
{
  "name": "Joséw Silva",
  "avatar": "https://media.istockphoto.com/illustrations/client-prime-white-round-button-illustration-id873164974",
  "contact": "(19)88d888-1111",
  "pay_day": 20,
  "establishment_id": 3
}

```

## PATCH client

Atualiza o cliente do estabelecimento.

`/establishment/<establishment_id>/client/<client_id>`

BODY:

```sh
{
  "name": "Hamero"
}
```

<br />
<br />

## ESTABLISHMENT

Rotas de estabelecimento.

## POST establishment

Cria um novo estabelecimento.

`/api/establishments/user/<int:user_id>`

## GET all establishments

Retorna todos os estabelecimentos do usuário.

`/api/establishments`

## GET one establishment

Retorna o estabelecimento do usuário pelo id do estabelecimento.

`/api/establishments/<int:id>`

## GET establishment by name

Retorna o estabelecimento do usuário pelo id do estabelecimento.

`/api/establishments/name/<name>`

## PATCH establishment

Atualiza o estabelecimento

`/api/establishments/<int:id>`

```sh
    {
    "name": "Mercearia",
    "url_logo": ""

    }
```

<br />
<br />

## PRODUCTS

Rota de produtos.

## POST

Cria um novo produto no estabelecimento.

`/api/establishments/products`

```sh
{
"name": "Batata",
"description": "batata frita",
"sale_price": 12,
 "cost_price":8,
 "unit_type":"kg",
 "url_img": "feerergerg",
 "establieshment_id":3,
 "categories": []

}
```

## GET products

Retorna os produtos do estabelecimento (id).

`/api/establishments/<establishment_id>/products`

## GET product by id

Retorna o produto (id) do estabelecimento

`/api/establishments/<establishment_id>/products/<product_id>`

## GET product query

Retorna o produto pesquisado.

`/api/establishments/<establishment_id>/products/query`

## PATCH product

Atualiza o produto do estabelecimento.

`/api/establishments/<establishment_id>/products/<product_id>`
<br />
<br />

## SALES

Rota de vendas.

## GET sale

Retorna a venda por id.

`/api/sales/<id>`

## GET sale by client

Retorna a venda por cliente

`/api/sales/client/<client_id>`

## POST sale

Cria nova venda.

`/api/sales`

## PATCH sale

Atualiza a venda (id).

`/api/sales/<int:id>`

## Sobre
