from bottle import route, view, request
import bottle
from src.facade.facade import Facade

facade = Facade()


@route('/')
@view('index')
def index():
    return


@route('/login', method='POST')
def login():
    nome = request.params['usuario']
    senha = request.params['senha']

    retorno = facade.PesquisaAlunoFacade(nome)

    if retorno:
        if retorno['senha'] == senha:
            bottle.redirect('/user_menu')
        else:
            bottle.redirect('/')
    else:
        bottle.redirect('/')
