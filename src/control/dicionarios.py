# encoding: utf-8

TIPO_USUARIOS = dict(
    administrador='0',
    gestor='1',
    diretor='2',
    coordenador='2.5',
    professor='3',
    responsavel='4',
    responsavel_varejo='5',
    aluno='6',
    aluno_varejo='7'
)

TIPO_USUARIOS_ID = {
    '7':'ALUNO VAREJO',
    '6':'ALUNO',
    '5':'RESPONSAVEL VAREJO',
    '4':'RESPONSAVEL',
    '3':'PROFESSOR',
    '2.5':'COORDENADOR',
    '2':'DIRETOR',
    '1':'GESTOR',
    '0':'ADMINISTRADOR'
}
TIPO_ITEM =dict(
    cor='1',
    rosto='2',
    acessorio='3',
    corpo='4'
)

TIPO_MEDALHA_NOME = {
    'SocioEmocional': '1',
    'Jogo':'2'
}

TIPO_MEDALHA_ID = {
    '1':'SocioEmocional',
    '2':'Jogo'
}


SERIE = {
    '0':'Pré-escola',
    '1':'1ª Ano',
    '2':'2ª Ano',
    '3':'3ª Ano',
    '4':'4ª Ano',
    '5':'5ª Ano'
}

PAGINA_INICIAL = dict(
    administrador='/administrador/pag_administrador',#'/gestao_aprendizagem'
    gestor='/gestao_aprendizagem',
    diretor='/gestao_aprendizagem',
    coordenador='/gestao_aprendizagem',
    professor='/gestao_aprendizagem',
    responsavel='/gestao_aprendizagem',
    responsavel_varejo='/gestao_aprendizagem',
    aluno='/aluno/area_aluno',
    aluno_varejo='/aluno/area_aluno'
)


TIPO_ESTRUTURA = dict(
    rede='1',
    escola='2',
    turma='3',
    item='4',
    medalha='5',
    historico='6',
    objeto_de_aprendizagem='7'
)

DICIPLINA = {
    '1' : 'Lingua Portuguesa',
    '2' : 'Matemática'
}

DICIPLINA_NOME = {
     'lingua Portuguesa' : '1',
     'matematica' : '2'
}

TIPO_OAS = {
    '1': 'MINI_GAME',
    '2': 'VIDEO',
    '3': 'CINEMATIC'
}

TIPO_OAS_ID = {
    'MINI_GAME': '1',
}

UNIDADES = {
    '1': 'Unidade 1',
    '2': 'Unidade 2',
    '3': 'Unidade 3',
    '4': 'Unidade 4',
    '5': 'Unidade 5',
    '6': 'Unidade 6',
    '7': 'Unidade 7',
    '8': 'Unidade 8'
}

PREMIO_JOGOS={
    '0':{'moedas':'1', 'xp':'0'},
    'facil':{'moedas':'2', 'xp':'0'},
    'medio':{'moedas':'3', 'xp':'1'},
    'dificil':{'moedas':'4', 'xp':'3'}
}

AVENTURAS_CONECTURMA = {
    '0':'****', #Ainda não tem na plataforma
    '1':{'aventurasAcessiveis': ["UV1AV1"]},
    '2':{'aventurasAcessiveis': ["UV1AV1", "UV1AV2"]},
    '3':{'aventurasAcessiveis': ["UV1AV1", "UV1AV2", "UV1AV3"]}
}


