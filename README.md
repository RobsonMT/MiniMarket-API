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
    <li><a href="#rotas">Rotas</a></li>
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

## Signup

Método: POST
<br />
Auth: user/admin
<br />
`/api/signup`
<br />
Body (JSON):
<br />

<code>
  {
<br />

"name": "marcelo",
<br />

"email": "marcelo@email.com",
<br />

"password": "123456",
<br />

"avatar": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/User_font_awesome.svg/2048px-User_font_awesome.svg.png",
<br />

"contact": "19 93588-3611"
<br />

}
</code>

<br />

## Sobre
