# encoding: utf-8

from model.historico_model import DbHistorico


class HistoricoFacade:

    def __init__(self):
        self.historico = DbHistorico()

    def create_historico_facade(self,**kwargs):
        return self.historico.create_historico(**kwargs)

    def update_historico_facade(self,**kwargs):
        '''
        futuro para acrescentar os dados de criaçao das coisas e os internos das funçoes usadas
        '''
        return self.historico.update_historico(**kwargs)

    def read_historico_facade(self):
        return self.historico.read_historico()

    def historico_de_dados_cadastrados_facade(self,hist_id:int,dicionari:dict):
        return self.historico.hist_dados_cadastrado(hist_id,dicionari)

    def ver_dados_cadastrados_facade(self,ide):
        return self.historico.ver_dados_cadastrados(ide)

    def search_historico_id_facade(self,id:int):
        return self.historico.search_historico_id(id)

    def search_historico_nome_facade(self,nome):
        return self.historico.search_historico_nome(nome)

    def search_historico_acao_facade(self,acao):
        return self.historico.search_historico_acao(acao)