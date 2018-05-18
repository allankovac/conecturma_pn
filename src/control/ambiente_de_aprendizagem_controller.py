from bottle import route,view, request, redirect, response,get
from facade.facade_main import Facade
from control.classes.permissao import permissao,usuario_logado
facade=Facade()

"""Tipo=6"""

@route('/aluno/area_aluno')
@view('caminho_aluno/jogar_conecturma')
def view_jogar_conecturma():
    """ pagina inicial apos login , que mostra os itens equipados no avatar"""
    if request.get_cookie("login", secret='2524'):
        usuario = usuario_logado()
        avatar = facade.avatar_facade(usuario['id'])
        if usuario['cor'] == "0":
            cor = 'default'
        else:
            cor =facade.search_estrutura_id_facade(avatar['cor'])['nome']

        if usuario['rosto'] == "0":
            rosto = 'default'
        else:
            rosto = facade.search_estrutura_id_facade(avatar['rosto'])['nome']
        if usuario['acessorio'] == "0":
            acessorio = 'default'
        else:
            acessorio = facade.search_estrutura_id_facade(avatar['acessorio'])['nome']
        if usuario['acessorio'] == "0":
            corpo = 'default'
        else:
            corpo = facade.search_estrutura_id_facade(avatar['corpo'])['nome']

        avatar_pecas = {'cor': cor,
                        'rosto': rosto,
                        'acessorio': acessorio,
                        'corpo': corpo}
        return dict(usuario=usuario.nome, avatar = avatar_pecas ,tipo="6")
    else:
        redirect('/')

@route('/aluno/loja')
@permissao('diretor')
@view('caminho_aluno/index_loja')
def index():
    """
    Mostra os itens comprados e os itens disponiveis para serem comprados na mesma pagina
    metodos usados : ja_tem_item_facade, read_estrutura_facade
    :return: um dicionario com os itens comprados e disponiveis , caso um item nao tenha sido criado previamente
    retorna um dicionario vazio"""

    #itens_comprados = facade.ja_tem_item_facade(request.get_cookie("login", secret='2524'))
    itens_comprados = []
    itens = facade.read_estrutura_facade('4')
    if itens:
        return dict(itens=itens, itens_comprados=str(itens_comprados))
    else:
        return dict(itens=False)

@route('/aluno/ver_itens_comprados')
@view('caminho_aluno/view_itens')
def ver_itens():
    """
    mostra os itens que o usuario tem posse
    chama os metodos : pesquisa_aluno_nome_facade, ver_item_comprado_facade e pesquisa_iten_facade
    cria uma lista com os ids dos itens do aluno

    :return: dicionario de itens
    """

    usuario = usuario_logado()
    print("APC L71",usuario['id'])
    itens_comprado = facade.ver_item_comprado_facade(usuario['id'])
    itens = []
    for y in itens_comprado:
        itens.append(facade.search_estrutura_id_facade(y))

    return dict(lista_itens=itens)


@route('/equipar_item', method='POST')
def equipar_item():
    """
    Equipar o avatar
    metodos chamados: pesquisa_aluno_nome_facade,search_estrutura_by_id e equipar_item_facade
    :return:
    """

    usuario = usuario_logado()

    id_item = request.forms['id']
    item = facade.search_estrutura_by_id(id_item)

    facade.equipar_item_facade(usuario['id'], item)

    redirect('/aluno/ver_itens_comprados')

@get('/jogos')
@permissao('aluno_varejo')
@view('ojogo')
def jogo():
    """
    jogo que recebe o parâmetro de qual botão foi clicado e armazena a quantidade de acertos
    :return: nome do jogo
    """

    jogo = request.params['n1']
    return dict(nome_jogo=jogo)

""" Controle do score """


@get('/ponto')
def ponto():
    """
    Recebe o nome do botão que o jogador clicou para o jogo o valor de 1 em caso de acerto
    incrementa nos pontos em cada jogo e manda um clique para ser acrescentado a cliques totais , para fins estatisticos

    :return:ao termino do jogo volta a pagina do menu
    """

    jogo = request.params['jogo']
    ponto = int(request.params['ponto'])
    usuario = usuario_logado()


    facade.ponto_jogo_facade(usuario, jogo, ponto)
    redirect('/')

    """ redirect('/jogos', BaseResponse.add_header(jogo=jogo ,value=jogo))"""

@route('aluno/ver_item')
@permissao('aluno_varejo')
@view('loja/ver_item')
def ver_item():
    """
    mostra os itens da loja , os ja criados
    :return:o dicionario com o read
    """

    read = facade.read_estrutura_facade('4')

    return dict(teste=read)


@get('/compras_loja')
def compras():
    """
    compra o item que esta na loja
    metodos usados: pesquisa_aluno_nome_facade,compra_item_facade
    :return:
    """

    id_item = request.params['id']
    usuario_logad = usuario_logado()
    facade.compra_item_facade(id_usuario=usuario_logad['id'], id_item=id_item)

    redirect('aluno/loja')
