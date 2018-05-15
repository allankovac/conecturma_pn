from bottle import route, view, request, redirect, response, get, template
from facade.facade_main import *

facade=Facade()

@route('/gestao_aprendizagem')
@view('caminho_observador/gestao_aprendizagem')
def view_gestao_aprendizagem():

    if request.get_cookie("login", secret='2525'):
        observador = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
        return dict(usuario = observador['nome'], tipo = observador['tipo'])


#                                            """BOTAO USUARIO"""


@route('/gestao_aprendizagem/usuario')
@view('usuario/index')
def view_usuario_index():
    """
    mostra todos os usuarios , escolas e redes cadastradas
    :return:
    """
    if request.get_cookie("login", secret='2525'):
        observador = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
        usuario = controller_index_usuario(observador['tipo'],observador['vinculo_escola'])
        rede, escola, turma = controller_filtro_opcoes(tipo_logado=observador['tipo'])
        return dict(observador_tipo=observador['tipo'], usuarios=usuario, redes=rede, escolas=escola, turmas=turma)
    else:
        print(facade.search_observador_facade(request.get_cookie("login",secret='2525')))
        redirect('/')

@route('/gestao_aprendizagem/usuario/redirect_cadastro')
def controller_redirect_cadastro():
    tipo_usuario = request.params['tipo_usuario']
    if tipo_usuario is '1':
        redirect('/observador/cadastro?tipo_observador=1')
    elif tipo_usuario is '2':
        redirect('/observador/cadastro?tipo_observador=2')
    elif tipo_usuario is '3':
        redirect('/observador/cadastro?tipo_observador=3')
    elif tipo_usuario is '6':
        redirect('/aluno/cadastro_aluno')
    else:
        redirect('/gestao_aprendizagem/usuario')

def controller_index_usuario(tipo_observador,vinculo_escola):
    aluno = facade.read_aluno_facade()
    observador = facade.search_observador_escola_listagem_facade(login=tipo_observador,vinculo_escola=vinculo_escola)
    usuario = []
    for a in aluno:
        a['tipo'] = tipo_usuario(a['tipo'])
        #a['vinculo_escola'] = facade.search_estrutura_id_facade(int(a['vinculo_escola']))['nome']
        #a['vinculo_rede'] = facade.search_estrutura_id_facade(int(a['vinculo_rede']))['nome']
        usuario.append(a)
    for o in observador:
        if o['tipo'] is not '0':
            if o['tipo'] is not '1':
                o['tipo'] = tipo_usuario(o['tipo'])
                o['vinculo_escola'] = facade.search_estrutura_id_facade(int(o['vinculo_escola']))['nome']
                o['vinculo_rede'] = facade.search_estrutura_id_facade(int(o['vinculo_rede']))['nome']
            else:
                #rede = facade.search_estrutura_facade(int(o['vinculo_rede']))
                o['tipo'] = tipo_usuario(o['tipo'])
                o['vinculo_escola'] = " "
                #o['vinculo_rede'] = rede['nome']

            usuario.append(o)

    return usuario

def controller_filtro_opcoes(tipo_logado):
    observador = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
    if tipo_logado is '0':
        rede = facade.read_estrutura_facade(tipo_estrutura='1')
        escola = facade.read_estrutura_facade(tipo_estrutura='2')
        turma = facade.read_estrutura_facade(tipo_estrutura='3')

        return rede, escola, turma

    elif tipo_logado is '1':
        rede = facade.search_estrutura_id_facade(id=int(observador['vinculo_rede']))
        escola = []
        turma = []
        for e in facade.search_estrutura_escola_by_rede_facade(vinculo_rede=str(rede['id'])):
            escola.append(e)
            for t in facade.search_estrutura_turma_by_escola_facade(vinculo_escola=str(e['id'])):
                    turma.append(t)

        return rede, escola, turma

    elif tipo_logado is '2':
        escola = facade.search_estrutura_id_facade(id=int(observador['vinculo_escola']))
        rede = facade.search_estrutura_id_facade(id=int(escola['vinculo_rede']))
        turma = []
        for t in facade.search_estrutura_turma_by_escola_facade(vinculo_escola=str(escola['id'])):
            turma.append(t)

        return rede, escola, turma

    """ NÃO ESTÁ PRONTO AINDA !!!!!!! elif tipo_logado is '3':
        escola = facade.search_escola_id_facade(id=int(observador['vinculo_escola']))
        rede = rede = facade.search_rede_facade(rede=escola['vinculo_rede'])
        turma = []



        return rede, escola, turma"""

@route('/aluno/cadastro_aluno')
@view('aluno/aluno_cadastro')
def aluno():

    if request.get_cookie("login", secret='2525'):
        observador = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
        if observador['tipo'] == '0':
            escolas = facade.read_estrutura_facade(tipo_estrutura="2")
            return dict(escolas=escolas, tipo_observador=observador['tipo'])
        elif observador['tipo'] == '1':
            escola = facade.read_escola_facade()
            escolas = []
            for e in escola:
                if e['vinculo_rede'] is observador['vinculo_rede']:
                    escolas.append(e)
            return dict(escolas=escolas, tipo_observador=observador['tipo'])
        elif observador['tipo'] == '2':
            escolas = facade.search_escola_id_facade(int(observador['vinculo_escola']))
            return dict(escolas=escolas, tipo_observador=observador['tipo'])

        elif observador['tipo'] == '3':
            escolas = facade.search_escola_id_facade(int(observador['vinculo_escola']))
            return dict(escolas=escolas, tipo_observador=observador['tipo'])
    else:
        redirect('/')

@route('/aluno_cadastro', method='POST')
def create_aluno():
    """
    Direcionamento a pagina para criar aluno buscando , na tpl os parâmetros usuário , senha e matricula
    Chama a funçao create_aluno_facade
    :return:
    """
    escola = request.forms['escola']
    vinculo_rede=facade.search_estrutura_id_facade(int(escola))
    if facade.create_aluno_facade(nome=request.forms['aluno_nome'], escola=escola, senha=request.forms['senha'],vinculo_rede=vinculo_rede['vinculo_rede']):
        redirect('/')
    else:
        print("deu erro na criação do ALuno")


def tipo_usuario(id_tipo):
    if id_tipo is '1':
        return "GESTOR"
    elif id_tipo is '2':
        return "DIRETOR"
    elif id_tipo is '3':
        return "PROFESSOR"
    elif id_tipo is '6':
        return "ALUNO"

@route('/observador/cadastro')
def view_observador_cadastro():
    tipo_observador = int(request.params['tipo_observador'])
    escola = facade.read_estrutura_facade(tipo_estrutura="2")
    rede = facade.read_estrutura_facade(tipo_estrutura="1")
    turma = facade.read_estrutura_facade(tipo_estrutura="3")

    if tipo_observador == 0:
        return template('observador/create_observador', tipo=tipo_observador)
    elif tipo_observador == 1:
        return template('observador/create_observador', tipo=tipo_observador, rede=rede)
    elif tipo_observador == 2:
        return template('observador/create_observador', tipo=tipo_observador, escola=escola)
    elif tipo_observador == 3:
        return template('observador/create_observador', tipo=tipo_observador, escola=escola, turma=turma)
    elif tipo_observador == 4:
        redirect('/observador')
    else:
        redirect('/observador')

@route('/observador/create_observador', method="POST")
def controller_observador_cadastro():
    """
    Cria um professor com nome , senha , telefone ,email e escola(recebe o id)
    :return:
    """
    tipo = request.params['tipo']
    nome = request.params['nome']
    senha = request.params['senha']
    telefone = request.params['telefone']
    cpf = request.params['cpf']
    email = request.params['email']
    escola = request.params['escola']
    rede = request.params['rede']
    turma = request.params['turma']
    if escola == 0:
        pass
    else:
        if filtro_cadastro(nome=nome, senha=senha, cpf=cpf,telefone=telefone, email=email, tipo=tipo):
            facade.create_observador_facade(nome=nome, senha=senha, telefone=telefone, cpf=cpf,email=email, tipo=tipo,
                                            escola=escola, rede=rede, vinculo_turma=turma)
        else:
            print("Erro para salvar")

@route('/observador/email_existe', method='POST')
def controller_checar_se_email_existe():
    email = request.params['teste_email']
    verificacao = facade.search_observador_email_facade(email=email)
    if verificacao is not None:
        return verificacao['email']
    else:
        return None


@get('/observador/editar')
def view_observador_update():
    nome = request.params['nome']
    observador = facade.search_observador_facade(nome)
    return template('observador/update_observador', id=observador['id'], nome=observador['nome'],
                    telefone=observador['telefone'], cpf=observador['cpf'], email=observador['email'])


def controller_observador_read():
    observadores = facade.read_observador_facade()
    return observadores


@route('/observador/update_observador', method='POST')
def controller_observador_update():
    facade.update_observador_facade(id=request.params['id'], nome=request.params['nome'],
                                    telefone=request.params['telefone'], cpf=request.params['cpf'],
                                    email=request.params['email'])
    redirect('/observador/read_observador')

def filtro_cadastro(nome, senha, telefone, cpf, email, tipo):
    valida = ValidaNome(ValidaSenha(ValidaTelefone(ValidaCpf(ValidaEmail(ValidaTipo(ValidaOk()))))))
    return valida.validacao(nome=nome, senha=senha, telefone=telefone, cpf=cpf, email=email, tipo=tipo)

# @route('/usuario/redirect_cadastro')
# def controller_redirect_cadastro():
#     tipo_usuario = request.params['tipo_usuario']
#     if tipo_usuario is '1':
#         redirect('/observador/cadastro?tipo_observador=1')
#     elif tipo_usuario is '2':
#         redirect('/observador/cadastro?tipo_observador=2')
#     elif tipo_usuario is '3':
#         redirect('/observador/cadastro?tipo_observador=3')
#     elif tipo_usuario is '6':
#         redirect('/aluno/cadastro_aluno')
#     else:
#         redirect('gestao_aprendizagem/usuario')
#
# def controller_index_usuario(tipo_observador,vinculo_escola):
#     aluno = facade.read_aluno_facade()
#     observador = facade.search_observador_escola_listagem_facade(login=tipo_observador,vinculo_escola=vinculo_escola)
#     usuario = []
#     for a in aluno:
#         a['tipo'] = tipo_usuario(a['tipo'])
#         #a['vinculo_escola'] = facade.search_estrutura_id_facade(int(a['vinculo_escola']))['nome']
#         #a['vinculo_rede'] = facade.search_estrutura_id_facade(int(a['vinculo_rede']))['nome']
#         usuario.append(a)
#     for o in observador:
#         if o['tipo'] is not '0':
#             if o['tipo'] is not '1':
#                 o['tipo'] = tipo_usuario(o['tipo'])
#                 o['vinculo_escola'] = facade.search_estrutura_id_facade(int(o['vinculo_escola']))['nome']
#                 o['vinculo_rede'] = facade.search_estrutura_id_facade(int(o['vinculo_rede']))['nome']
#             else:
#                 #rede = facade.search_estrutura_facade(int(o['vinculo_rede']))
#                 o['tipo'] = tipo_usuario(o['tipo'])
#                 o['vinculo_escola'] = " "
#                 #o['vinculo_rede'] = rede['nome']
#
#             usuario.append(o)
#
#     return usuario
#
# def controller_filtro_opcoes(tipo_logado):
#     observador = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
#     if tipo_logado is '0':
#         rede = facade.read_estrutura_facade(tipo_estrutura='1')
#         escola = facade.read_estrutura_facade(tipo_estrutura='2')
#         turma = facade.read_estrutura_facade(tipo_estrutura='3')
#
#         return rede, escola, turma
#
#     elif tipo_logado is '1':
#         rede = facade.search_estrutura_id_facade(id=int(observador['vinculo_rede']))
#         escola = []
#         turma = []
#         for e in facade.search_estrutura_escola_by_rede_facade(vinculo_rede=str(rede['id'])):
#             escola.append(e)
#             for t in facade.search_estrutura_turma_by_escola_facade(vinculo_escola=str(e['id'])):
#                     turma.append(t)
#
#         return rede, escola, turma
#
#     elif tipo_logado is '2':
#         escola = facade.search_estrutura_id_facade(id=int(observador['vinculo_escola']))
#         rede = facade.search_estrutura_id_facade(id=int(escola['vinculo_rede']))
#         turma = []
#         for t in facade.search_estrutura_turma_by_escola_facade(vinculo_escola=str(escola['id'])):
#             turma.append(t)
#
#         return rede, escola, turma
#
#     """ NÃO ESTÁ PRONTO AINDA !!!!!!! elif tipo_logado is '3':
#         escola = facade.search_escola_id_facade(id=int(observador['vinculo_escola']))
#         rede = rede = facade.search_rede_facade(rede=escola['vinculo_rede'])
#         turma = []
#
#
#
#         return rede, escola, turma"""
#
# def tipo_usuario(id_tipo):
#     if id_tipo is '1':
#         return "GESTOR"
#     elif id_tipo is '2':
#         return "DIRETOR"
#     elif id_tipo is '3':
#         return "PROFESSOR"
#     elif id_tipo is '6':
#         return "ALUNO"
#                     BOTAO DE MEDALHA


@route('/medalha_cadastro')
@view('observador/medalha_cadastro.tpl')
def cadastrar_medalha():
    """
    pagina de cadastro de medalha
    :return:
    """
    return


@route('/create_medalha', method='POST')
def controller_medalha_cadastro():

    nome = request.params['nome']
    tipo = request.params['tipos']
    facade.create_medalha_facade(nome=nome, tipo=tipo)
    redirect('/gestao_aprendizagem')

@route('/ler_medalha')
@view('observador/read_medalhas.tpl')
def read_de_medalha():
    medalhas = []

    for medalha in facade.read_medalha_facade():
        medalhas.append(medalha)

    return dict(medalhas=medalhas)



#                 BOTAO DE REDES


@route('/rede')
@view("rede/rede")
def view_index_rede():
    """
    pagina inicial de rede , que mostra , tambem , as redes disponiveis no banco
    metodos usados: controller_read_rede :interno:
    :return: Dicionario de redes
    """
    redes = controller_read_rede()
    return dict(redes=redes)


@route('/rede/create_rede')
@view('rede/create_rede')
def view_rede_cadastro():
    """
    Vizualizaçao da pagina de criar redes
    :return: vazio
    """
    return

@route('/rede/update_rede')
@view('modificar_rede')
def view_modificar_rede():
    pass


@route('/rede/criar_rede', method='POST')
def controller_create_rede():
    """
    Cria rede com os parametros de nome da rede e o telefone da mesma
    metodos usados:create rede facade
    :return:
    """
    nome = request.params['nome_rede']
    telefone = request.params['telefone']
    facade.create_estrutura_facade(nome, telefone)
    redirect('/rede')


def controller_read_rede():
    """
    pagina de ler as redes criadas , armazena os atributos da rede em uma entrada de dicionario
    :return: o dicionario com os atributos de rede a serem mostrados
    """
    redes = facade.read_estrutura_facade(tipo_estrutura='1')
    rede = []
    if redes is None:
        return None
    else:
        for x in redes:
            rede.append(x)

        return rede

@route('/escola')
@view('escola/index')
def view_escola_index():
    """
    view inicial de escola, mostrando as escolas cadastradas no sistema
    usa o metodo: controller_escola_read :interno:
    :return:dicionario com os valores da escola a serem mostrados
    """
    escola = controller_escola_read()
    return dict(escola=escola)

@route('/escola/escola_cadastro')
@view('escola/create_escola')
def cadastro_escola():
    observador1 = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
    if observador1['tipo'] == '1':
        rede = facade.search_estrutura_id_facade(int(observador1['vinculo_rede']))
        return dict(observador_tipo=observador1['tipo'], rede=rede)
    elif observador1['tipo'] == '0':
        rede = facade.read_estrutura_facade(tipo_estrutura='1')
        return dict(observador_tipo=observador1['tipo'], rede=rede)

@route('/escola/criar_escola', method='POST')
def view_escola_cadastro():
    observador = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
    if observador['tipo'] == '1':
        rede = int(observador['vinculo_rede'])
        print("pegou isso em rede", rede)
        nome = request.params['nome']
        telefone = request.params['telefone']
        cep = request.params['cep']
        estado = request.params['estado']
        uf = request.params['uf']
        numero = request.params['numero']
        if filtro_cadastro(nome, cep, numero, telefone, estado, uf):
            facade.create_escola_facade(nome=nome, telefone=telefone, cep=cep, estado=estado, uf=uf, numero=numero,
                                        vinculo_rede=rede)
            redirect("/escola")
    elif observador['tipo'] == '0':
        # rede = facade.search_rede_id_facade(int(observador['vinculo_rede']))
        nome = request.params['nome']
        telefone = request.params['telefone']
        cep = request.params['cep']
        estado = request.params['estado']
        uf = request.params['uf']
        numero = request.params['numero']
        rede_pertencente = request.params['rede']

        if filtro_cadastro(nome, cep, numero, telefone, estado, uf):
            facade.create_estrutura_facade(nome=nome, tipo_estrutura='2', telefone=telefone, cep=cep, estado=estado,
                                           uf=uf, numero=numero,
                                           vinculo_rede=rede_pertencente)
            # rede = facade.read_rede_facade()
            redirect("/escola")
        else:
            print("Erro para salvar escola")

def filtro_cadastro(nome, cep, numero, telefone, estado, uf):
    """
    impede que os parametros do cadastro sejam postados vazios
    :param nome: nome da escola
    :param telefone: telefone da escola
    :param rua: rua em que reside a escola
    :param numero: numero da casa da escola(na rua)
    :param estado: estado da escola
    :param cidade: cidade da escola
    :param cod_identificacao: codigo identificador da escola , no cadastro do governo
    :return: false se alguns desses parametros vier vazio e true se todos vierem preenchidos
    """

    return True

def controller_escola_read():
    """
    Cria uma lista , coloca as escolas do banco na lista para mostrar na tela
    metodos usados: read_escola_facade
    :return: a lista de escolas q serao mostradas
    """
    escolas = []
    escola = facade.read_estrutura_facade(tipo_estrutura='2')
    if escola is None:
        return None
    else:
        for e in escola:
            if int(e['vinculo_rede']) > 0:
                print("BB {} ".format(int(e['vinculo_rede'])))
                rede = facade.search_estrutura_id_facade(int(e['vinculo_rede']))
                e['vinculo_rede'] = rede['nome']
            escolas.append(e)
        return escolas

@route('/escola/update_escola', method='POST')
def controller_escola_update():
    """
    modifica os dados da escola
    :return:
    """
    facade.update_escola_facade(id=request.params['id'], nome=request.params['nome'], numero=request.params['numero'],
                                telefone=request.params['telefone'], estado=request.params['estado'],
                                cidade=request.params['cidade'], vinculo_rede=request.params['rede_pertencente'])
    redirect('/')

@get('/escola/editar')
def view_escola_update():
    """
    Edita os atributos de escola , recebendo o parametro de nome da escola
    metodos usados : pesquisa_escola_facade
    :return: o template referente a pagina de update
    """
    nome = request.params['nome']
    escolas = facade.search_escola_facade(nome)
    return template('escola/update_escola', id=escolas['id'], nome=escolas['nome'], numero=escolas['numero'],
                    estado=escolas['estado'], cidade=['cidade'],
                    telefone=escolas['telefone'], rua=escolas['rua'], rede_pertencente=escolas['rede_pertencente'],
                    cod_identificacao=escolas['cod_identificacao'])

#                   BOTAO DE TURMA

@route('/turma')
@view('turma/turma')
def view_turma():
    """
    Pagina inicial de turmas e q mostra as turmas ja cadastradas
    metodos utilizados : controller_read_ turma :interno dessa pagina:
    :return: dicionario com os parametros da turma a serem mostrados
    """
    turmas = controller_read_turma()
    return dict(turma=turmas)


""" Create Turma """


@route('/turma/turma_cadastro')
@view('turma/turma_cadastro')
def view_cadastrar_turma():
    """
    Pagina de cadastro de turma , mostra as escolas ja cadastradas no banco de dados
    metodos usados: read_escola_facade
    :return:o dicionario com as escolas
    """

    observador = facade.search_observador_facade(request.get_cookie("login", secret='2525'))
    if observador['tipo'] == '2':
        escola = facade.search_estrutura_id_facade(int(observador['vinculo_escola']))
        return dict(escolas=escola, observador_tipo = observador['tipo'])
    elif observador['tipo'] == '1':
        escola = []
        escolas = facade.read_estrutura_facade(tipo_estrutura='2')
        for e in escolas:
            if e['vinculo_rede'] is observador['vinculo_rede']:
                escola.append(e)

        return dict(escolas=escola, observador_tipo=observador['tipo'])
    elif observador['tipo'] == '0':
        escola = facade.read_estrutura_facade(tipo_estrutura='2')
        return dict(escolas=escola, observador_tipo=observador['tipo'])

@route('/turma/turma_update', method='POST')
def view_update_turma():
    """
    Pagina de cadastro de turma , mostra as escolas ja cadastradas no banco de dados
    metodos usados: read_escola_facade
    :return:o dicionario com as escolas
    """
    id = request.forms['id_turma']

    turma = facade.search_turma_id_facade(int(id))
    aluno = facade.search_aluno_escola_facade(turma['escola'])
    alunos = []
    for a in aluno:
        if a['vinculo_turma'] == '0':
            alunos.append(a)
    print(alunos)
    professor = facade.search_observador_professor_by_escola_facade(turma['escola'])
    professores = []
    for p in professor:
        if p['vinculo_turma'] is '0':
            professores.append(p)

    return template('turma/turma_update', turma=turma, aluno = alunos, professor = professores)

@route('/turma/turma_update_controller', method='POST')
def controller_update_turma():

    teste = request.forms

    turma = request.forms['turma']
    alunos = [aluno.split('_')[1] for aluno in teste if 'aluno' in aluno]
    professores = [professor.split('_')[1] for professor in teste if 'professor' in professor]

    if alunos is not '' or alunos is not []:
        for a in alunos:
            facade.aluno_in_turma_facade(id_aluno=int(a),vinculo_turma=turma)
        print(alunos)
    if professores is not '' or professores is not []:
        for p in professores:
            facade.obser(id_aluno=int(a),vinculo_turma=turma)
        print(alunos)

    redirect('/turma')

@route('/turma/cadastro_turma', method='POST')
def controller_create_turma():
    """
    """
    turma = request.forms['turma_nome']
    serie = request.forms['serie']
    escola = request.forms['escola']
    facade.create_estrutura_facade(nome=turma, tipo_estrutura='3',quem_criou=request.get_cookie("login", secret='2524'), serie=serie, vinculo_escola=escola)
    redirect('/turma')


def controller_read_turma():
    """
    Direciona para a pagina que mostra a turma e nomeia as series
    metodos usados: read_turma_facade
    :return: a entrada de dicionario que contem o id e o turma_nome
    """
    turmas = facade.read_estrutura_facade(tipo_estrutura='3')
    if turmas == None:
        return None
    else:

        turma = []
        for t in turmas:
            escola = facade.search_estrutura_id_facade(int(t['escola']))
            t['escola'] = escola['nome']
            t['serie'] = serie(t['serie'])
            turma.append(t)

        return turma


"""Turma Delete"""


@get('/deletar_turma')
def deletar_turma():
    """
    nao implementado
    :return:
    """
    facade.delete_turma_facade(request.params['id'])
    redirect('/turma')

def serie(id_serie):
    if id_serie == '0':
        return "Pré-escola"
    elif id_serie == '1':
        return "1ª Ano"
    elif id_serie == '2':
        return "2ª Ano"
    elif id_serie == '3':
        return "3ª Ano"
    elif id_serie == '4':
        return "4ª Ano"
    elif id_serie == '5':
        return "5ª Ano"