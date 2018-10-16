# encoding: utf-8

from model.jogo_model import DesempenhoJogo

class OaConcluidoFacade:
    def __init__(self):
        self.oaconcluido = DesempenhoJogo()

    def create_oa_concluido_facade(self, **kwargs):
        return self.oaconcluido.create_desempenho_jogo(**kwargs)

    def search_desempenho_concluido_id_aluno_facade(self, id_aluno):
        return self.oaconcluido.search_desempenho_concluido_id_aluno(id_aluno)

    def unidade_concluida_facade(self, id_aluno:int, unidade:str):
        return self.oaconcluido.unidade_concluida(id_aluno=id_aluno, unidade=unidade)

    def search_oa_facade(self,id_aluno:int,objeto_aprendizagem):
        return self.oaconcluido.search_oa(id_aluno,objeto_aprendizagem)

    def objeto_concluido_facade(self,id_aluno,objeto_aprendizagem):
        return self.oaconcluido.search_oa(id_aluno,objeto_aprendizagem)

    def unidade_teste_facade(self, id_aluno, unidade):
        return self.oaconcluido.unidade_teste(id_aluno=id_aluno, unidade=unidade)

    def oa_teste_facade(self, id_aluno, oa):
        return self.oaconcluido.oa_teste(id_aluno=id_aluno, oa=oa)

    def armazenar_dados_jogos_facade(self,id_obj,dados):
        return self.oaconcluido.armazenando_dados_jogo(id_obj,dados)