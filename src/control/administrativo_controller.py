# encoding: utf-8

from bottle import route, view, get, request, redirect, template
from control.classes.validar_cadastros_updates import *
from facade.facade_main import Facade
from control.gestao_aprendizagem_controller import *
from control.classes.permissao import permissao, usuario_logado
from control.dicionarios import TIPO_USUARIOS_ID

facade = Facade()

def controller_observador_cadastro():

    nome = request.params['nome']
    senha = request.params['senha']
    telefone = request.params['telefone']
    cpf = '0'
    email = request.params['email']
    tipo = request.params['tipo_observador']
    rede = '0'
    escola = '0'

    facade.create_observador_facade(nome=nome, senha=senha, telefone=telefone, cpf=cpf, email=email, tipo=tipo,
                                    rede=rede, escola=escola)
    redirect('/observador')



def view_adm():
    return


def pesquisar_aluno_turma():

    aluno_ = request.params['nome_do_aluno']
    turma_ = request.params['nome_da_turma']
    facade.pesquisa_aluno_turma_facade(aluno_, turma_)


def cadastro_item():

    facade.create_estrutura_facade(nome=request.forms.nome, tipo_item=request.forms.tipo, preco=request.forms.preco,
                                   tipo_estrutura='4')
    redirect('cadastrar_item')


def cadastro_descritor_view():
    return template('descritor/index')


def cadastro_descritor_controller():
    pass



def desativados():

    usuarios = []
    for h in facade.read_inativos_facade():
        if h['tipo_usuario'] != '0':
            h['tipo_usuario'] = TIPO_USUARIOS_ID[h['tipo_usuario']]
            h['tipo_aluno'] ='0'
        else:
            h['tipo_aluno'] = TIPO_USUARIOS_ID[h['tipo_aluno']]
            h['tipo_usuario'] = '0'
        usuarios.append(h)

    return dict(usuarios=usuarios)

def index_historico_controller():
    historico = facade.read_historico_facade()

    return dict(usuario=historico)