from bottle import route, template, request
from control.classes.permissao import permissao, usuario_logado
from control.observador_controller import Observador
from control.relatorios.relatorio_escola_controller import RelatorioEscola

path_template = 'gestao_aprendizagem/relatorios/escola/'


@route('/relatorios/escola')
@permissao('diretor')
def relatorio_turma_view(no_repeat=False):
    observador = Observador(observador_logado=usuario_logado())
    return template(path_template + 'relatorio_escola', tipo=observador.get_observador_tipo(),
                    escola=observador.get_escola())


@route('/relatorios/visualizar_relatorio_escola')
@permissao('diretor')
def relatorio_aluno(no_repeat=False):
    observador = Observador(observador_logado=usuario_logado())
    relatorio = RelatorioEscola()

    serie = request.params['serie']
    escolas = request.params['escola']

    escola = observador.get_escola(id_escola=escolas)
    descritores = relatorio.get_descritores(serie=serie)
    turmas = observador.get_turma(serie=serie, id_escola=escolas)

    turma = []
    for i in turmas:
        media_alunos = relatorio.get_media_alunos(turma=i['id'])
        i['media'] = []
        for z in relatorio.get_pontuacao_turma(medias=media_alunos):
            if z != -1:
                i['media'].append(int(z))
            else:
                i['media'].append(0)
        turma.append(i)
    media_escola = relatorio.get_media_escola(turma_media=turma, descritor=descritores)

    turma = []
    notas = []
    for index, i in enumerate(descritores):
        nota = []
        for z in turmas:
            if z['nome'] not in turma:
                turma.append(z['nome'])
            try:
                nota.append(str(z['media'][index]))
            except IndexError:
                pass
        notas.append(nota)

    return template(path_template + 'relatorio_escola_detalhe', media_geral = relatorio.media_geral(pontuacao=media_escola),
                    media_portugues=relatorio.media_portugues(pontuacao=media_escola),media_matematica=relatorio.media_matematica(pontuacao=media_escola),
                    tipo=observador.get_observador_tipo(),turma=turma, notas=notas, escola=escola,
                    porcentagem=media_escola, oa=descritores)

@route('/relatorios/selecao_serie')
@permissao('diretor')
def selecao_serie():
    observador = Observador(observador_logado=usuario_logado())

    return template(path_template + 'relatorio_selecao_serie', tipo=observador.get_observador_tipo(), escola=request.params['id'])


@route('/relatorios/relatorio_escola_impressao', method='POST')
def relatorio_impressao():
    from bottle import request
    from control.relatorios.relatorio_escola_controller import RelatorioEscola
    from control.dicionarios import DICIPLINA_NOME
    relatorio = RelatorioEscola()
    observador = Observador(observador_logado=usuario_logado())

    observador.get_turma(id_escola=observador)
    ultima_vez = []

    #novo for
    oa_mat = []
    pontos_mat = []
    oa_port = []
    pontos_port = []
    teste = 0
    for index,i in enumerate(relatorio.descritores):
        if i['disciplina'] == DICIPLINA_NOME['matematica']:
            try:
                pontos_mat.append(relatorio.porcentagem[teste])
                oa_mat.append(float(i['sigla_oa'][8:9] + "." + i['sigla_oa'][12]))
            except:
                pass
            teste+=1
        else:
            if i['sigla_oa'][9:11] != 'VC' and i['sigla_oa'][9:11] != 'CN':
                try:
                    pontos_port.append(relatorio.porcentagem[teste])
                    oa_port.append(float(i['sigla_oa'][8:9] + "." + i['sigla_oa'][12]))
                except:
                    pass
                teste+=1

    return template(path_template +'relatorio_escola_impressao', media_portugues=relatorio.media_portugues(),
                    aluno=aluno , oa_mat=oa_mat, oa_port=oa_port, pontos_mat= pontos_mat, pontos_port=pontos_port)


