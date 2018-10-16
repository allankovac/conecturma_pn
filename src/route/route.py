# encoding: utf-8

import os

from bottle import route, view, get, request, post, redirect, Bottle, delete

from control.administrativo_controller import index_historico_controller
from control.aluno_controller import Aluno_controler
from control.classes.permissao import permissao, algum_usuario_logado, usuario_logado
from facade.facade_main import Facade
# from model.historico_model import DbHistorico
from model.observador_model import DbObservador

facade = Facade()

"""
Rotas da Tela de Login
"""


@route('/')
@algum_usuario_logado
@view('login/index')
def view_login_index():
    return


@route('/login/login_observador', method='POST')
def login_observador_controller():
    from control.login_controller import login_observador_controller
    return login_observador_controller()


@route('/login/login_aluno', method='POST')
def login_aluno_controller():
    from control.login_controller import login_aluno_controller
    return login_aluno_controller()


@route('/esqueci_senha')
def view_esqueci_senha():
    from control.login_controller import view_esqueci_senha
    return view_esqueci_senha()


@route('/view_reformular_senha')
def view_reformular_senha():
    from control.login_controller import view_reformular_senha
    return view_reformular_senha()


@route('/controller_reformular_senha', method="POST")
def controller_esqueci_senha():
    from control.login_controller import controller_esqueci_senha
    return controller_esqueci_senha()


@route('/sair')
def controller_login_sair():
    from control.login_controller import controller_login_sair
    return controller_login_sair()


"""
                        ROTAS COM CAMINHO DO AMBIENTE DE APRENDIZAGEM
"""

@route('/aluno/area_aluno')
# @permissao('aluno_varejo')
@view('caminho_aluno/jogar_conecturma')
@permissao('aluno_varejo')
def view_ambiente_de_aprendizagem(no_repeat=False):
    from control.aprendizagem_controller import view_ambiente_de_aprendizagem
    return view_ambiente_de_aprendizagem()


@route('/aluno/guarda_roupa')
@permissao('aluno_varejo')
def view_guarda_roupa(no_repeat=False):
    from bottle import template
    from control.guarda_roupa_controller import Guarda_roupa

    if usuario_logado()['tipo'] >= '6':
        usuario = facade.search_aluno_id_facade(id_aluno=usuario_logado()['id'])
    else:
        usuario = facade.search_observador_id_facade(id=usuario_logado()['id'])

    if usuario['cor'] != '0':
        cor = facade.search_estrutura_id_facade(id=usuario['cor'])
    else:
        cor = '0'

    if usuario['rosto'] != '0':
        rosto = facade.search_estrutura_id_facade(id=usuario['rosto'])
    else:
        rosto = '0'

    if usuario['acessorio'] != '0':
        acessorio = facade.search_estrutura_id_facade(id=usuario['acessorio'])
    else:
        acessorio = '0'

    if usuario['corpo'] != '0':
        corpo = facade.search_estrutura_id_facade(id=usuario['corpo'])
    else:
        corpo = '0'

    guarda_roupa = Guarda_roupa(usuario_logado=usuario_logado())
    guarda_roupa.get_item_comprar()
    guarda_roupa.get_item_user_have()

    return template('caminho_aluno/guarda_roupa/index', usuario_logado=usuario_logado(), apelido=usuario['apelido'],
                    cor=cor, rosto=rosto, acessorio=acessorio, corpo=corpo, cristais=usuario['pontos_de_moedas'],
                    cores=guarda_roupa.get_cor(), rostos=guarda_roupa.get_rosto(),
                    acessorios=guarda_roupa.get_acessorio(), corpos=guarda_roupa.get_corpo(),
                    itens_usuario=guarda_roupa.get_itens_user())



@route('/comprar_item', method='POST')
@permissao('aluno_varejo')
def buy_item(no_repeat=False):
    from bottle import request
    from control.guarda_roupa_controller import Guarda_roupa

    guarda_roupa = Guarda_roupa(usuario_logado=usuario_logado())
    if guarda_roupa.buy_item(id_item=request.params['item']):
        return '1'
    else:
        return '0'


@route('/equipar_item', method='POST')
@permissao('aluno_varejo')
def equip_item(no_repeat=False):
    from bottle import request
    usuario = usuario_logado()
    item = []

    for i in request.params:
        if i != 'apelido':
            item.append(facade.search_estrutura_id_facade(id=request.params[i]))
    if request.params['apelido'] != '0' or request.params['apelido'] != "" or request.params['apelido'] != None:
        facade.set_apelido_facade(id=usuario['id'], apelido=request.params['apelido'])
    facade.equipar_item_facade(id=usuario['id'], itens=item)


@route('/ObterValoresHud', method='POST')
@permissao('aluno_varejo')
def valores_moedas_vidas_hud(no_repeat=False):
    aluno_c = Aluno_controler()
    return aluno_c.obter_moedas_e_vidas_hud(usuario=usuario_logado())


"""                                       FUNÇOES E ROTAS PARA FUNCIONAR O JOGO                             """
@route('/jogo')
def jogo():
    from bottle import template
    return template('jogo/index')


@route('/api/plataforma/obterUltimaConclusao', method='POST')
def obterUltimaConclusao():
    from control.aprendizagem_controller import obterUltimaConclusao
    return obterUltimaConclusao()


@route('/api/plataforma/verificarAcessoObjetoAprendizagem', method='POST')
def verificarAcessoObjetoAprendizagem():
    from control.aprendizagem_controller import verificarAcessoObjetoAprendizagem
    return verificarAcessoObjetoAprendizagem()


@route('/api/plataforma/verificarConclusoesObjetosAprendizagem', method='POST')
def verificarConclusoesObjetosAprendizagem():
    from control.aprendizagem_controller import verificarConclusoesObjetosAprendizagem
    return verificarConclusoesObjetosAprendizagem()


@route('/api/plataforma/registrarConclusao', method='POST')
def registrarConclusao():
    from control.aprendizagem_controller import registrarConclusao
    return registrarConclusao()


@route('/api/plataforma/obterPremiacao', method='POST')
def obterPremiacao():
    from control.aprendizagem_controller import obterPremiacao
    return obterPremiacao()


@route('/api/plataforma/verificarAcessoUnidade', method='POST')
def verificarAcessoUnidade():
    from control.aprendizagem_controller import verificarAcessoUnidade
    return verificarAcessoUnidade()


@route('/api/plataforma/verificarAcessoAventura', method='POST')
def verificarAcessoAventura():
    from control.aprendizagem_controller import verificarAcessoAventura
    return verificarAcessoAventura()


"""                             ROTAS DO CAMINHO DE GESTAO DE APRENDIZAGEM                               """


@route('/gestao_aprendizagem')
# @permissao('responsavel_varejo')
@view('gestao_aprendizagem/gestao_aprendizagem')
@permissao('responsavel_varejo')
def view_gestao_aprendizagem(no_repeat=False):
    from control.gestao_aprendizagem_controller import view_gestao_aprendizagem
    return view_gestao_aprendizagem()


@route('/gestao_aprendizagem/usuario')
# @permissao('professor')
@view('gestao_aprendizagem/usuario/usuario')
@permissao('responsavel_varejo')
def view_usuario_index(no_repeat=False):
    from control.gestao_aprendizagem_controller import view_usuario_index
    return view_usuario_index()


@route('/usuario/cadastro_usuario', method='POST')
@permissao('professor')
def cadastro_usuario(no_repeat=False):
    from control.gestao_aprendizagem_controller import cadastro_usuario

    if no_repeat:
        usuario = {}
        for i in request.params:
            usuario[i] = request.params.getunicode(i)
        return usuario
    return cadastro_usuario()


@route('/checar_login_existente', method='POST')
def checar_se_existe():
    from facade.facade_main import Facade
    facade = Facade()
    nome_login = request.params['login']
    existe_usuario = facade.search_aluno_primeiro_nome_facade(nome_login)
    if existe_usuario == []:
        return dict(resposta='nao existe login')
    else:
        return dict(resposta='existe login')


@route('/check_mudanca_cadastro', method='POST')
def check_changes():
    '''
    metodo para usar no ajax do javascript checar_se_algo_mudou_obs(id) , que serve para o formulario de usuarios
    :return: uma mensagem informando se os dados recebidos sao iguais ou nao as do banco
    '''
    id = request.params['id']
    nome = request.params['nome']
    email = request.params['email']
    aff = []
    for id in id:
        if id.isdigit():
            aff.append(id)
    id = ''.join(aff)

    observador = facade.search_observador_id_facade(id)

    if observador['nome'] == nome and observador['email'] == email:
        return dict(resposta=' nop chuck testa , sem mudança')
    elif observador['nome'] != nome or observador['email'] != email:
        return dict(resposta='teve mudança', nome=observador['nome'])


@route('/check_mudanca_cadastro_aluno', method='POST')
def check_change_mudanca_alun():
    id = request.params['id']
    nome = request.params['nome']
    login = request.params['login']
    aff = []
    for id in id:
        if id.isdigit():
            aff.append(id)
    id = ''.join(aff)

    aluno = facade.search_aluno_id_facade(int(id))

    if aluno['nome'] == nome and aluno['nome_login'] == login:
        return dict(resposta=' nop chuck testa , sem mudança')
    elif aluno['nome'] != nome or aluno['email'] != aluno:
        return dict(resposta='teve mudança', nome=aluno['nome'])


@route('/aluno/update_aluno', method='POST')
def aluno_edit():
    from control.dicionarios import TIPO_ESTRUTURA
    id = request.params['id']
    nome = request.params.getunicode('nome')
    nome_login = request.params['login']
    try:
        turma_al = request.params['turma']
        print('turma_al', turma_al)
        aluno_c = Aluno_controler()
        return aluno_c.update_aluno(id=id, nome=nome, nome_login=nome_login, turma=turma_al)
    except KeyError:
        aluno_c = Aluno_controler()
        return aluno_c.update_aluno(id=id, nome=nome, nome_login=nome_login)


@get('/observador/editar')
@permissao('professor')
def view_observador_update(no_repeat=False):
    from control.gestao_aprendizagem_controller import view_observador_update
    return view_observador_update()


@route('/observador/update_observador', method='POST')
@permissao('professor')
def controller_observador_update(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_observador_update
    return controller_observador_update()


@route('/observador/email_existe', method='POST')
@permissao('professor')
def controller_checar_se_email_existe(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_checar_se_email_existe
    return controller_checar_se_email_existe()


@route('/medalha_cadastro')
@view('observador/medalha_cadastro.tpl')
def cadastrar_medalha(no_repeat=False):
    return


@route('/create_medalha', method='POST')
def controller_medalha_cadastro():
    from control.gestao_aprendizagem_controller import controller_medalha_cadastro
    return controller_medalha_cadastro()


@route('/ler_medalha')
# @permissao('professor')
@view('observador/medalha_index.tpl')
@permissao('professor')
def read_de_medalha(no_repeat=False):
    from control.gestao_aprendizagem_controller import read_de_medalha
    return read_de_medalha()


@route('medalha/aluno-medalhas', method='POST')
def medalhas_aluno():
    from control.aprendizagem_controller import read_medalha_album
    aluno = usuario_logado()['id']
    aluno_medalhas = read_medalha_album(aluno)
    return dict(aluno_medalhas=aluno_medalhas)


@route('/aluno/medalhas')
# @permissao('aluno_varejo')
@view('caminho_aluno/medalhas.tpl')
@permissao('aluno_varejo')
def read_medalha_aluno():
    from control.aprendizagem_controller import read_medalha_album, getMedalhas
    aluno = usuario_logado()
    if int(aluno['tipo']) < 6:
        return getMedalhas(aluno)
    else:
        return read_medalha_album(aluno['id'])


@route('/rede')
# @permissao('gestor')
@view("gestao_aprendizagem/rede/rede")
@permissao('gestor')
def view_index_rede(no_repeat=False):
    from control.gestao_aprendizagem_controller import view_index_rede
    return view_index_rede()


@route('/rede/criar_rede', method='POST')
@permissao('gestor')
def controller_create_rede(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_create_rede
    return controller_create_rede(no_repeat)


@route('/rede/editar_rede', method='POST')
@permissao('gestor')
def controller_editar_rede(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_editar_rede
    if no_repeat:
        estrutura = request.params
        return estrutura
    return controller_editar_rede()


@route('/escola')
@view('gestao_aprendizagem/escola/escola')
def view_escola_index(no_repeat=False):
    from control.gestao_aprendizagem_controller import view_escola_index
    return view_escola_index()


@route('/escola/criar_escola', method='POST')
@permissao('gestor')
def controller_escola_cadastro(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_escola_cadastro
    return controller_escola_cadastro(no_repeat)


@route('/escola/editar_escola', method='POST')
@permissao('diretor')
def controller_escola_editar(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_escola_update
    if no_repeat:
        estrutura = request.params
        return estrutura
    return controller_escola_update()


@route('/deletar_estrutura', method='POST')
@permissao('diretor')
def controller_estrutura_deletar(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_estrutura_delete
    return controller_estrutura_delete()


@route('/turma')
# @permissao('professor')
@view('gestao_aprendizagem/turma/turma')
@permissao('professor')
def view_turma(no_repeat=False):
    from control.gestao_aprendizagem_controller import view_turma
    return view_turma()


@route('/turma/cadastro_turma', method='POST')
@permissao('diretor')
def controller_create_turma(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_create_turma
    return controller_create_turma(no_repeat)


@route('/turma/update_turma', method='POST')
@permissao('professor')
def controller_turma_editar(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_edit_turma
    return controller_edit_turma(no_repeat)


@route('/turma/turma_update_controller', method='POST')
@permissao('diretor')
def controller_update_turma(no_repeat=False):
    from control.gestao_aprendizagem_controller import controller_update_turma
    return controller_update_turma(no_repeat)


@route('/turma/entregar_medalha_aluno', method='POST')
@permissao('professor')
def controller_entregar_medalha_aluno():
    from control.gestao_aprendizagem_controller import controller_entregar_medalha_aluno
    return controller_entregar_medalha_aluno()


@route('/turma/entregar_medalha_todos_alunos', method='POST')
@permissao('professor')
def entregar_medalha_todos_alunos():
    from control.gestao_aprendizagem_controller import entregar_medalha_todos_alunos
    return entregar_medalha_todos_alunos()


@route('/cadastro_descritor_view')
@view('descritor/index.tpl')
def descritores():
    return


@route('/relatorios/aluno')
# @permissao('professor')
@view('gestao_aprendizagem/relatorios/aluno/relatorio_aluno')
@permissao('professor')
def relatorio_aluno_view(no_repeat=False):
    from control.relatorio_controller import Relatorio
    from control.gestao_aprendizagem_controller import get_nome_turma

    relatorio = Relatorio()
    relatorio.get_alunos(usuario_online_dados=usuario_logado(), nome_turma=get_nome_turma)

    return dict(tipo=usuario_logado()['tipo'], alunos=relatorio.alunos)


@route('/relatorios/visualizar_relatorio_aluno')
@view('gestao_aprendizagem/relatorios/aluno/relatorio_aluno_detalhe')
def relatorio_aluno(no_repeat=False):
    from bottle import request
    from facade.facade_main import Facade
    from control.relatorio_controller import Relatorio

    relatorio = Relatorio()

    aluno = facade.search_aluno_id_facade(id_aluno=request.params['aluno'])
    turma = facade.search_estrutura_id_facade(id=aluno['vinculo_turma'])

    relatorio.get_descritores(serie=turma['serie'])
    relatorio.get_desempenho(descritores=relatorio.descritores, aluno=aluno)
    relatorio.convert_nivel_for_numeric()
    relatorio.set_color_face()
    relatorio.set_pontuacao_porcentagem()

    return dict(tipo=usuario_logado()['tipo'], aluno=aluno, oa=relatorio.descritores, porcentagem=relatorio.porcentagem,
                pontos=relatorio.porcentagem_solo, vezes=relatorio.vezes_jogada)


@route('/trazer_oas')
@view('gestao_aprendizagem/relatorios/aluno/relatorio_table.tpl')
def levar_oas_matematica():
    from control.relatorio_controller import Relatorio
    relatorio = Relatorio()

    aluno = facade.search_aluno_id_facade(id_aluno=request.params['aluno'])
    turma = facade.search_estrutura_id_facade(id=aluno['vinculo_turma'])

    relatorio.get_matematica_or_portugues_descritor(serie=turma['serie'], diciplina=request.params['diciplina'])
    relatorio.get_desempenho(descritores=relatorio.descritores, aluno=aluno)
    relatorio.convert_nivel_for_numeric()
    relatorio.set_color_face()
    relatorio.set_pontuacao_porcentagem()

    return dict(oa=relatorio.descritores, aluno=aluno, porcentagem=relatorio.porcentagem,
                pontos=relatorio.porcentagem_solo)


"""
Rotas da Tela de do gestão de aprendizagem
"""


@route('/observador/create_observador_administrador', method="POST")
@permissao('administrador')
def controller_observador_cadastro(no_repeat=False):
    from control.administrativo_controller import controller_observador_cadastro
    return controller_observador_cadastro()


@route('/administrador/pag_administrador')
@view('areas_administrativo.tpl')
@permissao('administrador')
def view_adm(no_repeat=False):
    return index_historico_controller()


@route('/pesquisa_aluno_in_turma')
def pesquisar_aluno_turma():
    from control.administrativo_controller import pesquisar_aluno_turma
    return pesquisar_aluno_turma()


@route('/loja/cadastrar_item')
# @permissao('administrador')
@view('loja/cadastrar_item.tpl')
@permissao('administrador')
def cadastrar_item(no_repeat=False):
    return


@route('/cadastro_item', method='post')
def cadastro_item():
    from control.administrativo_controller import cadastro_item
    return cadastro_item()


@route('/administrador/cadastro_descritor_view')
def cadastro_descritor_view():
    from control.administrativo_controller import cadastro_descritor_view
    return cadastro_descritor_view()


@route('administrativo/cadastro_descritor_controller', method='post')
def cadastro_descritor_controller():
    pass


@route('/usuarios_inativados')
@view('inativados/inativados.tpl')
def index_desativados():
    return


@route('/usuarios_deletados')
@view('inativados/usuarios_inativados')
def desativados():
    from control.administrativo_controller import desativados
    return desativados()


@get('/new_senha')
def new_password():
    from control.administrativo_controller import new_password
    return new_password()


@route('/novasenha', method='post')
def novasenha():
    from control.administrativo_controller import novasenha
    return novasenha()


@post('/upload_img')
def upload():
    try:
        upload_file = request.POST['uploadfile']
        ext = upload_file.filename.split('.')[1]
        nome_foto = upload_file.filename = usuario_logado()['nome'] + '.' + ext
        if ext not in ('png', 'jpeg', 'jpg'):
            redirect('/gestao_aprendizagem2')
        usuario = DbObservador.load(usuario_logado()['id'])
        usuario.nome_foto_perfil = nome_foto
        usuario.save()
        upload_file.save('view/app/fotos_usuarios', overwrite=True)
        redirect('/gestao_aprendizagem')
    except AttributeError:
        redirect('/gestao_aprendizagem')


@route('/salvar_css_foto', method='post')
def salvar_css_foto():
    observador = DbObservador.load(usuario_logado()['id'])
    observador.aux_css_foto = request.params['posicao_foto']
    observador.save()


