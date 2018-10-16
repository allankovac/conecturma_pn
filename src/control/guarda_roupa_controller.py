# encoding: utf-8

from facade.facade_main import Facade
from control.dicionarios import TIPO_ITEM, TIPO_ESTRUTURA

class Guarda_roupa(object):
    def __init__(self, usuario_logado):
        self.usuario_logado = usuario_logado
        self.facade = Facade()
        self.cor = []
        self.rosto = []
        self.acessorio = []
        self.corpo = []
        self.itens_user = []

    def get_cor(self):
        return self.cor

    def set_cor(self, cores):
        self.cor = cores

    def get_rosto(self):
        return self.rosto

    def set_rosto(self, rostos):
        self.rosto = rostos

    def get_acessorio(self):
        return self.acessorio

    def set_acessorio(self, acessorios):
        self.acessorio = acessorios

    def get_corpo(self):
        return self.corpo

    def set_corpo(self, corpos):
        self.corpo = corpos

    def get_itens_user(self):
        return self.itens_user

    def set_itens_user(self, itens_user):
        self.itens_user = itens_user

    def get_item_comprar(self):
        itens = self.facade.read_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'])
        for i in itens:
            if i['tipo_item'] == TIPO_ITEM['cor']:
                self.cor.append(i)
            elif i['tipo_item'] == TIPO_ITEM['rosto']:
                self.rosto.append(i)
            elif i['tipo_item'] == TIPO_ITEM['acessorio']:
                self.acessorio.append(i)
            else:
                self.corpo.append(i)

    def get_item_user_have(self):
        if self.usuario_logado['tipo'] > '5':
            itens = self.facade.get_itens_student_facade(id=self.usuario_logado['id'])
        else:
            itens = self.facade.get_itens_responsaveis_facade(id=self.usuario_logado['id'])

        for i in itens:
            self.itens_user.append(i.decode('utf-8'))


    def buy_item(self, id_item):
        if self.usuario_logado['tipo'] <'6':
            usuario = self.facade.search_observador_id_facade(id=self.usuario_logado['id'])
        else:
            return self.facade.compra_item_facade(id_item=id_item, id_usuario=self.usuario_logado['id'])

