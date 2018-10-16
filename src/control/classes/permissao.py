# encoding: utf-8

from bottle import redirect, response, request
from datetime import datetime
from control.dicionarios import *
from facade.historico_facade import HistoricoFacade
from facade.facade_main import Facade
from passlib.hash import sha512_crypt


from model.historico_model import DbHistorico

"""Constante para a key de hash temporariamente"""

KEY_HASH = 'gu3 j0st0çur4'


class Login_Observador(object):

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def login(self):
        facade = Facade()

        hash = self.gerar_hash()
        response.set_cookie("KIM", hash, path='/', secret=KEY_HASH)

        observador_logado = facade.search_observador_email_facade(email=self.email)
        if observador_logado != None:
            if observador_logado['email'] == self.email:
                if sha512_crypt.verify(self.senha, observador_logado['senha']):
                    response.set_cookie("BUMBA", observador_logado, path='/', secret=hash)
                    now = datetime.now()
                    facade.login_date_facade(observador_logado['id'], now)
                    facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['historico'],
                                                   nome_usuario=observador_logado['nome'],
                                                   tipo_usuario=observador_logado['tipo'])

                    return PAGINA_INICIAL[TIPO_USUARIOS_ID[observador_logado['tipo']].lower()]
                else:
                    return '/'
            else:
                return '/'
        else:
            print("Usuario não encontrado !")

    def gerar_hash(self):
        """
        Usa um algoritmo aleatório para criar um numero de matricula de 5 números

        :return: O numero da matricula do aluno
        """
        from random import randrange

        hash = []
        for i in range(0, 5):
            hash.append(randrange(1, 9))
        matricula = ''.join(str(x) for x in hash)
        return matricula


class Login_Aluno(object):
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def login(self):
        facade = Facade()
        hash = self.gerar_hash()
        print('nome',self.nome, self.senha)
        aluno = facade.search_aluno_nome_login_facade(nome_login=self.nome.upper())
        print(aluno)
        if aluno['nome_login'] == self.nome.upper():
            if aluno['senha'] == self.senha:
                response.set_cookie("KIM", hash, path='/', secret=KEY_HASH)
                """aluno_logado = dict(
                    id=aluno['id'],
                    nome=aluno['nome'],
                    tipo=aluno['tipo_aluno'],
                    vinculo_rede=aluno['vinculo_rede'],
                    vinculo_escola=aluno['vinculo_escola'],
                    vinculo_turma=aluno['vinculo_turma'],
                    # ultimo_oa = aluno['ultimo_objeto_aprendizagem'],
                    ultima_unidade= aluno['ultima_unidade'],
                    ultima_aventura= aluno['ultima_aventura'],
                    moeda=aluno['pontos_de_moedas'],
                    xp=aluno['pontos_de_vida']
                )"""
                print('entrei aqui')
                response.set_cookie("BUMBA", aluno, path='/', secret=hash)
                return PAGINA_INICIAL[tipo_observador(aluno['tipo'])]
        else:
            return '/'


    def gerar_hash(self):
        """
        Usa um algoritmo aleatório para criar um numero de matricula de 5 números

        :return: O numero da matricula do aluno
        """
        from random import randrange

        hash = []
        for i in range(0, 5):
            hash.append(randrange(1, 9))
        matricula = ''.join(str(x) for x in hash)
        return matricula

def update_cookie(premio):
    banana = request.get_cookie("KIM", secret=KEY_HASH)
    que = request.get_cookie("BUMBA", secret=banana)

    que['moeda'] = premio['moedas']
    que['xp'] = premio['xp']
    return PAGINA_INICIAL[tipo_observador(que['tipo'])]

def usuario_logado():
    banana = request.get_cookie("KIM", secret=KEY_HASH)
    que = request.get_cookie("BUMBA", secret=banana)

    return que


def algum_usuario_logado(function):
    def decorator(*args, **kwargs):
        banana = request.get_cookie("KIM", secret=KEY_HASH)
        que = request.get_cookie("BUMBA", secret=banana)
        if que and banana:
            redirect(PAGINA_INICIAL[TIPO_USUARIOS_ID[que['tipo']].lower()])
        else:
            return function(*args, **kwargs)

    return decorator


def permissao(quem_tem_permissao):
    def observador(function):
        def decorator(*args, **kwargs):
            banana = request.get_cookie("KIM", secret=KEY_HASH)
            que = request.get_cookie("BUMBA", secret=banana)
            if banana and que:
                if TIPO_USUARIOS[quem_tem_permissao] >= que['tipo']:
                    try:
                        histo = HistoricoFacade()
                        if 'get'in function.__name__ or 'lista' in function.__name__:
                            pass
                        elif 'view' in function.__name__:
                            histo.create_historico_facade(acao=function.__name__, nome_usuario=usuario_logado()['nome'],
                                                          momento=datetime.now())
                        elif 'controller' in function.__name__:

                            retorno_da_func = function(observador=usuario_logado(),no_repeat=True)
                            histo.create_historico_facade(acao=function.__name__, nome_usuario=usuario_logado()['nome'],
                                                          momento=datetime.now())
                        else:
                            retorno_da_func=function(no_repeat=True)

                            histo.create_historico_facade(acao=function.__name__,nome_usuario=usuario_logado()['nome'],momento=datetime.now())
                            # teste=histo.search_historico_nome_facade('administrador')
                            histo.historico_de_dados_cadastrados_facade(usuario_logado()['id'],retorno_da_func)
                    except Exception as e:
                        print('erro',e)
                    return function(*args, **kwargs)
                else:
                    redirect('/error403')
            else:
                redirect('/')

        return decorator

    return observador

def tipo_observador(tipo):
    # return {
    #     '0': 'administrador',
    #     '1': 'gestor',
    #     '2': 'diretor',
    #     '3': 'professor',
    #     '4': 'responsavel',
    #     '5': 'responsavel_varejo',
    #     '6': 'aluno',
    #     '7': 'aluno_varejo',
    # }
    if tipo == '0':
        return 'administrador'
    elif tipo == '6':
        return 'aluno'
    elif tipo == '7':
        return 'aluno_varejo'
    elif tipo == '3':
        return 'professor'
    elif tipo == '5':
        return 'responsavel_varejo'
    elif tipo == '4':
        return 'responsavel'
    elif tipo == '2':
        return 'diretor'
    elif tipo == '1':
        return 'gestor'
