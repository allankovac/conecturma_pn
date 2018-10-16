# encoding: utf-8

from bottle import route, request, template
from facade.facade_main import Facade
from control.classes.permissao import usuario_logado, permissao
from control.dicionarios import TIPO_USUARIOS_ID, TIPO_ESTRUTURA

facade = Facade()

@route('/filtro_usuario', method='POST')
def filtro_usuarios():
    rede = request.params['rede']
    escola = request.params['escola']
    turma = request.params['turma']
    tipo_usuario = request.params['tipo_usuario']
    usuario_tipo = usuario_logado()

    if turma == '0' and escola == '0' and rede != '0' and tipo_usuario == '0':
        usuarios = filtro_com_selecao_de_rede(rede)

    elif turma == '0' and escola != '0' and rede == '0' and tipo_usuario == '0':
        usuarios = filtro_com_selecao_de_escola(escola)

    elif turma != '0' and escola == '0' and rede == '0' and tipo_usuario == '0':
        usuarios = filtro_com_selecao_de_turma(turma)
    elif turma == '0' and escola == '0' and rede == '0' and tipo_usuario != '0':
        usuarios = filtro_com_selecao_usuario(tipo_usuario)

    return template('bottle/usuario/bottle_usuario_read_usuarios.tpl', usuarios=usuarios)

@route('/filtro_pesquisa', method='POST')
def filtro_pesquisa():
    rede = request.params['rede']
    escola = request.params['escola']
    turma = request.params['turma']
    tipo_usuario = request.params['tipo_usuario']
    usuario_tipo = usuario_logado()

    if usuario_tipo['vinculo_rede'] != '0':
        redes = rede
    else:
        redes = facade.read_estrutura_facade(TIPO_ESTRUTURA['rede'])

    if turma == '0' and escola == '0' and rede != '0' and tipo_usuario == '0':
        escolas = filtro_escolas_de_acordo_com_rede(rede=rede)
        turmas = filtro_turmas_de_acordo_com_rede(rede=rede)

    elif turma == '0' and escola != '0' and rede == '0' and tipo_usuario == '0':
        escolas = filtro_default_escolas()
        turmas = filtro_turma_de_acordo_com_escola(escola)
        if turmas == None or "":
            turmas = []

    elif turma != '0' and escola == '0' and rede == '0' and tipo_usuario == '0':
        turmas = filtro_default_turmas()
        escolas = filtro_default_escolas()

    elif turma == '0' and escola == '0' and rede == '0' and tipo_usuario != '0':
        escolas = filtro_default_escolas()
        turmas = filtro_default_turmas()

    else:

        escolas = filtro_default_escolas()
        turmas = filtro_default_turmas()

    return template('bottle/usuario/bottle_usuario_filtros.tpl', escolas=escolas, turmas=turmas,
                    observador_tipo=usuario_tipo['tipo'], redes=redes)

def filtro_com_selecao_de_rede(rede):
    usuarios = []
    aluno = facade.search_aluno_by_rede_facade(vinculo_rede=rede)
    for a in aluno:
        a['email'] = ''
        a['vinculo_rede'] = get_nome_rede(a['vinculo_rede'])
        a['vinculo_escola'] = get_nome_escola(a['vinculo_escola'])
        a['vinculo_turma'] = get_nome_turma(a['vinculo_turma'])
        a['tipo'] = TIPO_USUARIOS_ID[a['tipo']]
        usuarios.append(a)

    observador = facade.search_observador_by_rede_facade(vinculo_rede=rede)
    for o in observador:
        o['vinculo_rede'] = get_nome_rede(o['vinculo_rede'])
        o['vinculo_escola'] = get_nome_escola(o['vinculo_escola'])
        o['vinculo_turma'] = get_nome_turma(o['vinculo_turma'])
        o['tipo'] = TIPO_USUARIOS_ID[o['tipo']]
        usuarios.append(o)

    return usuarios

def filtro_com_selecao_de_escola(escola):
    usuarios = []
    aluno = facade.search_aluno_escola_facade(vinculo_escola=escola)

    for a in aluno:
        a['email'] = ''
        a['vinculo_rede'] = get_nome_rede(a['vinculo_rede'])
        a['vinculo_escola'] = get_nome_escola(a['vinculo_escola'])
        a['vinculo_turma'] = get_nome_turma(a['vinculo_turma'])
        a['tipo'] = TIPO_USUARIOS_ID[a['tipo']]
        usuarios.append(a)

    observador = facade.search_observador_escola(vinculo_escola=escola)
    for o in observador:
        o['email'] = ''
        o['vinculo_rede'] = get_nome_rede(o['vinculo_rede'])
        o['vinculo_escola'] = get_nome_escola(o['vinculo_escola'])
        o['vinculo_turma'] = get_nome_turma(o['vinculo_turma'])
        o['tipo'] = TIPO_USUARIOS_ID[o['tipo']]
        usuarios.append(o)

    return usuarios

def filtro_com_selecao_de_turma(turma):
    usuarios = []
    aluno = facade.search_aluno_by_turma_facade(turma)
    for a in aluno:
        a['email'] = ''
        a['vinculo_rede'] = get_nome_rede(a['vinculo_rede'])
        a['vinculo_escola'] = get_nome_escola(a['vinculo_escola'])
        a['vinculo_turma'] = get_nome_turma(a['vinculo_turma'])
        a['tipo'] = TIPO_USUARIOS_ID[a['tipo']]
        usuarios.append(a)

    observador = facade.search_observador_turma(turma)
    for o in observador:
        o['vinculo_rede'] = get_nome_rede(o['vinculo_rede'])
        o['vinculo_escola'] = get_nome_escola(o['vinculo_escola'])
        o['vinculo_turma'] = get_nome_turma(o['vinculo_turma'])
        o['tipo'] = TIPO_USUARIOS_ID[o['tipo']]
        usuarios.append(o)

    return usuarios

def filtro_com_selecao_usuario(tipo_usuario):
    usuarios = []

    if int(tipo_usuario) < 6:
        observador = facade.search_observador_tipo_facade(tipo=tipo_usuario)
        for o in observador:
            o['vinculo_rede'] = get_nome_rede(o['vinculo_rede'])
            o['vinculo_escola'] = get_nome_escola(o['vinculo_escola'])
            o['vinculo_turma'] = get_nome_turma(o['vinculo_turma'])
            o['tipo'] = TIPO_USUARIOS_ID[o['tipo']]
            usuarios.append(o)
    else:
        aluno = facade.read_aluno_facade()
        for a in aluno:
            a['vinculo_rede'] = get_nome_rede(a['vinculo_rede'])
            a['vinculo_escola'] = get_nome_escola(a['vinculo_escola'])
            a['vinculo_turma'] = get_nome_turma(a['vinculo_turma'])
            a['tipo'] = TIPO_USUARIOS_ID[a['tipo']]
            usuarios.append(a)

    return usuarios

def filtro_default_escolas():
    escolas = facade.read_estrutura_facade(TIPO_ESTRUTURA['escola'])
    return escolas

def filtro_default_turmas():
    turmas = facade.read_estrutura_facade(TIPO_ESTRUTURA['turma'])
    return turmas

def filtro_escolas_de_acordo_com_rede(rede):
    escolas = facade.search_estrutura_escola_by_rede_facade(rede)
    return escolas

def filtro_turmas_de_acordo_com_rede(rede):
    turmas = facade.search_estrutura_turma_by_rede_facade(rede)
    return turmas

def filtro_turma_de_acordo_com_escola(escola):
    turmas = facade.search_estrutura_turma_by_escola_facade(escola)
    return turmas

def get_nome_rede(vinculo_rede):
    rede_nome = facade.search_estrutura_id_facade(vinculo_rede)['nome']

    return rede_nome

def get_nome_escola(vinculo_escola):
    escola_nome = facade.search_estrutura_id_facade(vinculo_escola)
    return escola_nome['nome']

def get_nome_turma(vinculo_turma):
    turma_nome = facade.search_estrutura_id_facade(vinculo_turma)['nome']

    return turma_nome
