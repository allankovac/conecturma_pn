# encoding: utf-8

from model.estrutura_model import DbEstrutura


class EstruturaFacade:

    def __init__(self):
        self.estrutura = DbEstrutura()


    def create_estrutura_facade(self, **kwargs):
        return self.estrutura.create_estrutura(**kwargs)

    def read_estrutura_facade(self, tipo_estrutura):
        return self.estrutura.read_estrutura(tipo_estrutura=tipo_estrutura)

    def update_estrutura_facade(self,**kwargs):

        return self.estrutura.update_estrutura(**kwargs)

    def delete_estrutura_facade(self, id):

        return self.estrutura.delete_estrutura(id)

    def search_estrutura_facade(self, tipo_estrutura, nome):
        return self.estrutura.search_estrutura(tipo_estrutura=tipo_estrutura, nome= nome)

    def search_estrutura_id_facade(self, id):
        return self.estrutura.search_estrutura_id(id=id)

    def search_estrutura_escola_by_rede_facade(self,vinculo_rede):
        return self.estrutura.search_escola_by_rede(vinculo_rede=vinculo_rede)

    def search_estrutura_turma_by_rede_facade(self,vinculo_rede):
        return self.estrutura.search_turma_by_rede(vinculo_rede=vinculo_rede)

    def search_estrutura_turma_by_escola_facade(self,vinculo_escola):
        return self.estrutura.search_turma_by_escola(vinculo_escola=vinculo_escola)

    def search_oa_by_type_and_aventura_facade(self, aventura, disciplina):
        return self.estrutura.search_oa_by_type_and_aventura(aventura=aventura, disciplina=disciplina)

    def search_descritor_serie_facade(self, serie):
        return self.estrutura.search_descritor_serie(serie=serie)

    def search_descritor_serie_diciplina_facade(self, serie, diciplina):
        return self.estrutura.search_descritor_serie_diciplina(serie=serie, diciplina=diciplina)

    def get_itens_for_type_facade(self, type_item):
        return self.estrutura.get_itens_for_type(type_item=type_item)

    def get_itens_free_facade(self):
        return self.estrutura.get_itens_free()

    # def ja_tem_item_facade(self, usuario_logado):
    #
    #     return self.estrutura.ja_possui_item(usuario_logado=usuario_logado)

    # def anotacoes_observador_turma_facade(self, id_estrutura,mensagem):
    #     return self.estrutura.func_anotacoes_estrutura_turma(id_estrutura,mensagem)
    #
    # def anotacoes_observador_escola_facade(self, id_estrutura,mensagem):
    #     return self.estrutura.func_anotacoes_estrutura_escola(id_estrutura,mensagem)
    #
    # def anotacoes_observador_rede_facade(self,id_estrutura,mensagem):
    #     return self.estrutura.func_anotacoes_estrutura_rede(id_estrutura,mensagem)

