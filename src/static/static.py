# encoding: utf-8

from bottle import route, static_file

@route('/static/<filename>')
def css(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/css')

@route('/static/fontes/<filename>')
def fontes(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/fontes')

@route('/static/js/<filename>')
def js(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/js')

@route('/static/img/<filename>')
def img(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/img')

@route('/static/fotos_usuarios/<filename>')
def img(filename):
    return static_file(filename, root='././view/app/fotos_usuarios')


@route('/static/img/body/<filename>')
def img_body(filename):
    return static_file(filename, root='././view/app/img/body')

@route('/static/img/acessorio/<filename>')
def img_acessorio(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/img/acessorio')

@route('/static/img/corpo/<filename>')
def img_corpo(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/img/corpo')

@route('/static/img/rosto/<filename>')
def img_rosto(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/img/rosto')


@route('/static/img/menu/<filename>')
def img_menu(filename):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(filename, root='././view/app/img/menu')

@route ('/static/img/medalha/<filename>')
def img_medalha_jogo(filename):
    return static_file(filename, root='././view/app/img/medalha/jogo')

@route('/static/medalha/<filename>')
def img_medalha(filename):
    return static_file(filename, root='././view/app/img/medalha')

@route ('/static/img/medalha/socio/<filename>')
def img_medalha_socio(filename):
    return static_file(filename, root='././view/app/img/medalha/socio')

@route('/GLOBAL/<path:path>')
def global_path(path):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(path, root='././jogo/GLOBAL')

@route('/GLOBAL/player')
def global_player():
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(root='././jogo/GLOBAL/player')

@route('/ASSETS/<path:path>')
def assets_path(path):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(path, root='././jogo/ASSETS')

@route('/ASSETS_2/<path:path>')
def assets_path(path):

    return static_file(path, root='././jogo/ASSETS_2')

@route('/UV1/<path:path>')
def uv1_path(path):
    """
    ligaçao com o arquivo css
    :param filename:o caminho para onde esta o css
    :return:
    """
    return static_file(path, root='././jogo/UV1')



