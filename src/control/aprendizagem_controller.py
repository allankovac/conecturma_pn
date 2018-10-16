# encoding: utf-8

import json
from bottle import route, view, request, redirect, response, get, template

from control.gestao_aprendizagem_controller import convertendo_str_in_dict
from facade.facade_main import Facade
from control.classes.permissao import permissao, usuario_logado
from control.dicionarios import *

facade = Facade()



def itens_cadastrados_sistema():
    itens = facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'])
    return itens


def itens_usuario_tem():
    itens = facade.ver_item_comprado_facade(id_usuario=usuario_logado()['id'])
    return itens


def obterUltimaConclusao():
    retorno = {
        'objetoAprendizagem': '',
        'unidade': '',
        'aventura': '',
        'universo': 'UV1'
    }
    return retorno


def verificarAcessoObjetoAprendizagem():
    usuario = usuario_logado()
    parametros = parametros_json_jogos(request.params.items())
    print('verificar acesso OA ',parametros)
    if int(usuario['tipo']) < 6:
        retorno = {'objetosAprendizagemAcessiveis': parametros['objetosAprendizagem']}
    else:
        cn_final = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa='{}CN02'.format(parametros['objetosAprendizagem'][0:9]))
        if cn_final != []:
            retorno = {'objetosAprendizagemAcessiveis': parametros['objetosAprendizagem']}
        else:
            teste = []
            for i in parametros['objetosAprendizagem']:

                desempenho_oa = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa=i)
                if desempenho_oa == []:

                    teste.append(i)
                    break
                else:
                    teste.append(i)
            retorno = {'objetosAprendizagemAcessiveis': teste}
    return retorno


def verificarConclusoesObjetosAprendizagem():

    usuario = usuario_logado()
    parametros = parametros_json_jogos(request.params.items())
    print('parametros conclusao OA',parametros)
    if int(usuario['tipo']) < 6:
        retorno = {'objetosConcluidos': parametros['objetosAprendizagem']}

    else:
        cn_final = facade.oa_teste_facade(id_aluno=str(usuario['id']),
                                          oa='{}CN02'.format(parametros['objetosAprendizagem'][0:9]))
        if cn_final != []:
            retorno = {'objetosConcluidos': parametros['objetosAprendizagem']}
        else:
            teste = []

            for i in parametros['objetosAprendizagem']:
                desempenho_oa = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa=i)
                try:
                    print('desempenho oa1',desempenho_oa[0])
                    print('desempenho oa',desempenho_oa[0]['jogo_jogado'])
                    nivel_jogo = convertendo_str_in_dict(desempenho_oa[0]['jogo_jogado'][0])
                    if desempenho_oa == []:
                        print("desempenho",convertendo_str_in_dict(desempenho_oa[0]['jogo_jogado'][0]))
                    elif len(desempenho_oa[0]['jogo_jogado'])== 3:
                        teste.append(i)
                except Exception as e:
                    print('errio',e)


            retorno = {'objetosConcluidos': teste}

    return retorno

def view_ambiente_de_aprendizagem():
    usuario = usuario_logado()
    if usuario['tipo'] == TIPO_USUARIOS['aluno']:
        jogador = facade.search_aluno_id_facade(id_aluno=usuario['id'])
        vida = jogador['pontos_de_vida']
        moedas = jogador['pontos_de_moedas']

    else:
        jogador = facade.search_observador_id_facade(id=usuario['id'])
        # vida = jogador['pontos_de_vida']
        # moedas = jogador['pontos_de_moedas']

        if jogador['cor'] != '0':
            cor = facade.search_estrutura_id_facade(id=jogador['cor'])['image_name']
        else:
            cor = jogador['cor']

        if jogador['rosto'] != '0':
            rosto = facade.search_estrutura_id_facade(id=jogador['rosto'])['image_name']
        else:
            rosto = jogador['rosto']
        if jogador['acessorio'] != '0':
            acessorio = facade.search_estrutura_id_facade(id=jogador['acessorio'])['image_name']
        else:
            acessorio = jogador['acessorio']
        if jogador['corpo'] != '0':
            corpo = facade.search_estrutura_id_facade(id=jogador['corpo'])['image_name']
        else:
            corpo = jogador['corpo']

        vida = jogador['pontos_de_vida']
        moedas = jogador['pontos_de_moedas']
    avatar = set_avatar_jogador(jogador)

    return dict(apelido=jogador['apelido'], vida=vida, moedas=moedas, cor=avatar['cor'], rosto=avatar['rosto'],
                acessorio=avatar['acessorio'], corpo=avatar['corpo'])

def set_avatar_jogador(jogador):
    if jogador['cor'] != '0':
        cor = facade.search_estrutura_id_facade(id=jogador['cor'])['image_name']
    else:
        cor = jogador['cor']

    if jogador['rosto'] != '0':
        rosto = facade.search_estrutura_id_facade(id=jogador['rosto'])['image_name']
    else:
        rosto = jogador['rosto']
    if jogador['acessorio'] != '0':
        acessorio = facade.search_estrutura_id_facade(id=jogador['acessorio'])['image_name']
    else:
        acessorio = jogador['acessorio']
    if jogador['corpo'] != '0':
        corpo = facade.search_estrutura_id_facade(id=jogador['corpo'])['image_name']
    else:
        corpo = jogador['corpo']

    return dict(cor=cor, rosto=rosto, acessorio=acessorio, corpo=corpo)


def registrarConclusao():
    """responsavel por desbloquear o proximo OA"""
    usuario = usuario_logado()
    dados_jogo= parametros_json_jogos(request.params.items())
    print('todos dados jogo',dados_jogo)
    if usuario['tipo'] == TIPO_USUARIOS['aluno'] :
        if len(dados_jogo['niveis'])==3:
            print('dados jogo ',dados_jogo['niveis'][len(dados_jogo['niveis'])-1]['termino'])
            premios={
                'OA': is_oa,
                'VC': is_vc_or_cn,
                'CN': is_vc_or_cn
            }
            # if autorizaçao_professor()==True:

            return premios[parametros_json_jogos(request.params.items())['objetoAprendizagem'][9:11]]\
            (aluno=usuario['id'],parametros=parametros_json_jogos(request.params.items()),
             oa=parametros_json_jogos(request.params.items())['objetoAprendizagem'])

        elif dados_jogo['niveis'][len(dados_jogo['niveis'])-1]==True:
            print('dados jogo1 ', dados_jogo['niveis'][len(dados_jogo['niveis']) - 1]['termino'])
            premios = {
                'OA': is_oa,
                'VC': is_vc_or_cn,
                'CN': is_vc_or_cn
            }
            # if autorizaçao_professor()==True:

            return premios[parametros_json_jogos(request.params.items())['objetoAprendizagem'][9:11]] \
                (aluno=usuario['id'], parametros=parametros_json_jogos(request.params.items()),
                 oa=parametros_json_jogos(request.params.items())['objetoAprendizagem'])

        else:
            premios = {
                'OA': is_oa,
                'VC': is_vc_or_cn,
                'CN': is_vc_or_cn
            }

            return premios[parametros_json_jogos(request.params.items())['objetoAprendizagem'][9:11]] \
                (aluno=usuario['id'], parametros=parametros_json_jogos(request.params.items()),
                 oa=parametros_json_jogos(request.params.items())['objetoAprendizagem'])
    else:
        gamificacao = gamificacao_moeda_xp(parametros=parametros_json_jogos(request.params.items()))
        premios = {
            'medalhas': [''],
            'moedas': gamificacao['moedas'],
            'xp': gamificacao['xp']
        }
        return premios



def obterPremiacao():
    parametros = parametros_json_jogos(request.params.items())
    print('obter premiaçao',parametros)
    usuario = usuario_logado()
    if usuario['tipo'] == TIPO_USUARIOS['aluno']:
        aluno = facade.search_aluno_id_facade(id_aluno=usuario['id'])
        retorno = {
            'moedas': int(aluno['pontos_de_moedas']),
            'xp': int(aluno['pontos_de_vida'])
        }
    else:
        observador = facade.search_observador_id_facade(id=usuario['id'])
        retorno = {
            'moedas': int(observador['pontos_de_moedas']),
            'xp': int(observador['pontos_de_vida'])
        }

    return retorno

def verificarAcessoUnidade():
    usuario = usuario_logado()
    parametros = parametros_json_jogos(request.params.items())

    if int(usuario['tipo']) < 6:
        retorno = {'unidadesAcessiveis': parametros['unidades']}
    else:
        desempenho_aluno = facade.search_desempenho_concluido_id_aluno_facade(id_aluno=str(usuario['id']))
        if desempenho_aluno == []:
            retorno = {'unidadesAcessiveis': [parametros['unidades'][0]]}
        else:
            acesso_unidade = []
            for i in parametros['unidades']:
                desempenho_unidade = facade.unidade_teste_facade(id_aluno=str(usuario['id']), unidade=i)
                if desempenho_unidade == []:
                    acesso_unidade.append(i)
                    break
                else:
                    desempenho_oa = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa='{}OA06'.format(i))
                    if desempenho_oa == []:
                        acesso_unidade.append(i)

                        break
                    else:
                        acesso_unidade.append(i)
            retorno = {'unidadesAcessiveis': acesso_unidade}
    return retorno

# def verificarAcessoUnidade():
#     usuario = usuario_logado()
#     parametros = parametros_json_jogos(request.params.items())
#     if int(usuario['tipo']) < 6:
#         retorno = {'unidadesAcessiveis': parametros['unidades']}
#     else:
#         desempenho_aluno = facade.search_desempenho_concluido_id_aluno_facade(id_aluno=str(usuario['id']))
#         if desempenho_aluno == []:
#             retorno = {'unidadesAcessiveis': [parametros['unidades'][0]]}
#         else:
#             acesso_unidade = []
#             for i in parametros['unidades']:
#                 desempenho_unidade = facade.unidade_teste_facade(id_aluno=str(usuario['id']), unidade=i)
#                 if desempenho_unidade == []:
#                     acesso_unidade.append(i)
#                     break
#                 else:
#                     desempenho_oa = facade.oa_teste_facade(id_aluno=str(usuario['id']), oa='{}OA06'.format(i))
#                     if desempenho_oa == []:
#                         acesso_unidade.append(i)
#
#                         break
#                     else:
#                         acesso_unidade.append(i)
#             retorno = {'unidadesAcessiveis': acesso_unidade}
#     return retorno

def verificarAcessoAventura():
    from control.dicionarios import AVENTURAS_CONECTURMA
    usuario = usuario_logado()

    if int(usuario['tipo']) < 6:
        parametros = parametros_json_jogos(request.params.items())
        return AVENTURAS_CONECTURMA['3']
    else:
        from control.dicionarios import AVENTURAS_CONECTURMA
        serie_turma = facade.search_estrutura_id_facade(int(usuario['vinculo_turma']))
        return AVENTURAS_CONECTURMA[serie_turma['serie']]

def is_oa(aluno, parametros, oa):
    from control.classes.permissao import update_cookie
    gamificacao = gamificacao_moeda_xp(parametros)

    premios = {
        'medalhas': gamificacao_medalha(aluno, oa=oa),
        'moedas': gamificacao['moedas'],
        'xp': gamificacao['xp']
    }

    create_or_update_oa(id_aluno=aluno, unidade=oa[0:9], objeto_aprendizagem=oa,
                        parametros=parametros['niveis'])

    facade.gravar_premiacao(aluno, premios)
    update_cookie(premios)

    return premios

def is_vc_or_cn(aluno, parametros, oa):
    create_or_update_oa(id_aluno=aluno, unidade=oa[0:9], objeto_aprendizagem=oa,
                        parametros=parametros['niveis'])

    premios = {
        'medalhas': [],
        'moedas': [],
        'xp': []
    }

    return premios

def gamificacao_moeda_xp(parametros):
    from control.dicionarios import PREMIO_JOGOS

    ponto = pegar_maior_pontuacao(parametros['niveis'])
    if ponto:
        return PREMIO_JOGOS[ponto['nivel']]
    else:
        return PREMIO_JOGOS['0']


def gamificacao_medalha(usuario_id, oa):

    medalhas = []
    oa_concluidos = facade.search_desempenho_concluido_id_aluno_facade(id_aluno=str(usuario_id))
    medalhas.append(primeiro_jogo(facade.oa_teste_facade(id_aluno=str(usuario_id),oa='UV1AV1UD1OA01')))
    if len(oa_concluidos) >= 10:
        medalhas.append(dose_dupla(oa_concluidos))
    medalhas.append(dezena(usuario_id=str(usuario_id), oa=oa))
    medalhas.append(fera_da_Matemática(oa=oa))
    medalhas.append(fera_da_lingua_portuguesa(oa=oa))
    medalhas.append(musical(id_aluno=str(usuario_id),oa=oa))
    if 'OA' in oa:
        medalhas.append(de_novo(id_aluno=str(usuario_id), oa=oa))

    medalhas.append(magia_da_matematica(id_aluno=str(usuario_id), aventura=oa[0:6]))
    medalhas.append(magia_da_lingua_portuguesa(id_aluno=str(usuario_id), aventura=oa[0:6]))
    return testa_medalha_false(medalhas)

def testa_medalha_false(medalhas):
    retorno = []
    for i in medalhas:
        if i != False and i != None:
            retorno.append(i)

    return retorno

def testar_se_ja_medalha(id_usuario, medalha):
    pass


""" INICIO DOS METODOS REFERENTES A MEDALHAS"""

def primeiro_jogo(oa_concluido):

    if oa_concluido == []:
        return '11'
    else:
        return False


def dose_dupla(oa_concluido):

    medalha = 0

    for i in oa_concluido:
        if len(i['jogo_jogado']) > 1:
            medalha += 1
    if medalha == 10:
        return '12'
    else:
        return False


def dezena(usuario_id, oa):
    oas = facade.oa_teste_facade(id_aluno=usuario_id, oa=oa)
    if oas != None:
        for oa in oas :
            teste = len(oa['jogo_jogado'])
            if teste == 10:
                return '13'
            else:
                return False
    else:
        return False


def fera_da_Matemática(oa):
    if oa == 'UV1AV1UD1OA05' or oa == 'UV1AV2UD1OA05' or oa == 'UV1AV3UD1OA05':
        return '14'
    else:
        return False


def fera_da_lingua_portuguesa(oa):
    if oa == 'UV1AV1UD1OA06' or oa == 'UV1AV2UD1OA06' or oa == 'UV1AV3UD1OA06':
        return '15'
    else:
        return False


def musical(id_aluno,oa):
    aluno=facade.oa_teste_facade(id_aluno=id_aluno,oa='{}VC01'.format(oa[0:9]))
    if aluno != []:
        return '16'
    else:
        return False


def de_novo(id_aluno,oa):
    aluno = facade.oa_teste_facade(id_aluno=id_aluno,oa='{}VC01'.format(oa[0:9]))
    for i in aluno:

        if len(i['jogo_jogado']) >= 3:
            return '17'
        else:
            return False

def magia_da_matematica(id_aluno, aventura):

    oa = facade.search_oa_by_type_and_aventura_facade(aventura='UV1AV1', disciplina=DICIPLINA_NOME['matematica'])
    oas_terminandos_dificel = 0
    for i in oa:
        oa_terminados = facade.oa_teste_facade(id_aluno=id_aluno, oa =i)
        for z in oa_terminados:
            dificuldade = z['jogo_jogado'][len(z['jogo_jogado'])-1]
            if dificuldade['nivel'] == 'dificil':
                oas_terminandos_dificel += 1
            else:
                oas_terminandos_dificel = 0

    if oas_terminandos_dificel == 5:
        return '19'
    else:
        return False

def magia_da_lingua_portuguesa(id_aluno, aventura):

    oa = facade.search_oa_by_type_and_aventura_facade(aventura='UV1AV1', disciplina=DICIPLINA_NOME['lingua Portuguesa'])
    oas_terminandos_dificel = 0
    for i in oa:
        oa_terminados = facade.oa_teste_facade(id_aluno=id_aluno, oa=i)
        for z in oa_terminados:
            dificuldade = z['jogo_jogado'][len(z['jogo_jogado']) - 1]
            if dificuldade['nivel'] == 'dificil':
                oas_terminandos_dificel += 1
            else:
                oas_terminandos_dificel = 0

    if oas_terminandos_dificel >= 5:
        return '20'
    else:
        return False



def create_or_update_oa(id_aluno, unidade, objeto_aprendizagem, parametros):
    oa_existe = facade.objeto_concluido_facade(id_aluno=str(id_aluno), objeto_aprendizagem=objeto_aprendizagem)
    if oa_existe == None:

        facade.create_oa_concluido_facade(id_aluno=str(id_aluno), unidade=unidade,
                                          objeto_aprendizagem=objeto_aprendizagem)

        create_or_update_oa(id_aluno=str(id_aluno), unidade=unidade, objeto_aprendizagem=objeto_aprendizagem,
                            parametros=parametros)
    else:
        ponto = pegar_maior_pontuacao(parametros)
        if ponto != False:
            facade.armazenar_dados_jogos_facade(oa_existe['id'], ponto)
        else:
            facade.armazenar_dados_jogos_facade(oa_existe['id'], parametros)


def pegar_maior_pontuacao(parametros):
    teste = False
    for i in parametros:
        print('pegar maior pontuaçao', parametros)
        try:
            if i['termino'] == True:
                teste = i
                print('rodou com termino',teste,i)
        except Exception as exu:
            print('excessao',exu)
            if i['percentualConcluido']==100:
                i['termino']=True
                teste=i
            else:
                i['termino']=False
                teste=i
            print('entrei na excessao',exu,i['termino'],i)

    return teste


def parametros_json_jogos(parametro):

    for p in parametro:
        parametros = list(p)[0]
    parametros = json.loads(parametros)

    return parametros

def getMedalhas(aluno):
    medalha_socio = []
    medalha_jogo = []
    todas_medalhas = facade.read_estrutura_facade(TIPO_ESTRUTURA['medalha'])
    for i in todas_medalhas:
        if i['tipo_medalha'] == '1':
            medalha_socio.append(i)
        else:
            medalha_jogo.append(i)

    print('hie',len(todas_medalhas),len(medalha_socio),len(medalha_jogo))


    return dict(medalha_aluno=todas_medalhas,medalha_jogo=medalha_jogo,medalha_socio=medalha_socio,medalha_recente=[],aluno_id=aluno,usuario=usuario_logado())


# Resgatando Medalhas e Medalhas que o Aluno possui
def read_medalha_album(aluno):
    from control.gestao_aprendizagem_controller import convertendo_str_in_dict
    medalha_socio = []
    medalha_jogo = []
    medalha_aluno = []

    for i in facade.search_aluno_id_facade(id_aluno=aluno)['medalha']:
        i = convertendo_str_in_dict(str=i.decode('utf-8'))
        medalha_aluno.append(i['id_medalha'])

    todas_medalhas= facade.read_estrutura_facade(TIPO_ESTRUTURA['medalha'])
    for medalha in todas_medalhas:
        if medalha['tipo_medalha']== '1':
            medalha_socio.append(medalha)

        else:
            medalha_jogo.append(medalha)
    medalha_recente = []
    medalha_ultima = []
    if medalha_aluno != []:

        if len(medalha_aluno) > 4:
            z = medalha_aluno[len(medalha_aluno) - 4:len(medalha_aluno)]
        else:
            z = medalha_aluno

        for i in medalha_socio:
            if str(i['id']) in z:
                medalha_recente.append(i)
        for i in medalha_jogo:
            if str(i['id']) in z:
                medalha_recente.append(i)

        '''variavel medalha_recente da problema se n tiver medalha, ou se so tiver uma , pelo que parece '''
        try:
            medalha_ultima = medalha_ultima[len(medalha_recente) -1]
        except Exception as e:
            print('que ser esse erro? olhe depois , por favor',e)
    return dict(medalha_socio=medalha_socio,medalha_jogo=medalha_jogo,medalha_recente=medalha_recente,medalha_aluno=medalha_aluno,medalha_ultima=medalha_ultima,usuario=usuario_logado())

