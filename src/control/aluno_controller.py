# encoding: utf-8
from control.classes.permissao import usuario_logado
from control.dicionarios import TIPO_USUARIOS
from facade.facade_main import Facade

facade = Facade()




class Aluno_controler(object):


    def update_aluno(self,id,nome,nome_login,turma='0'):
        return facade.update_aluno_facade(id=id,nome=nome,nome_login=nome_login,turma=turma)

    def obter_moedas_e_vidas_hud(self,usuario):
        usuario = usuario_logado()
        if usuario['tipo'] == TIPO_USUARIOS['aluno']:
            jogador = facade.search_aluno_id_facade(id_aluno=usuario['id'])
            vida = jogador['pontos_de_vida']
            moedas = jogador['pontos_de_moedas']
        else:
            jogador = facade.search_observador_id_facade(id=usuario['id'])
            vida = jogador['pontos_de_vida']
            moedas = jogador['pontos_de_moedas']
        return dict(vida=vida, moedas=moedas)