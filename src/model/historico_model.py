# encoding: utf-8

from walrus import *
from random import randrange

db = Database(host='localhost', port=6379, db=0)


class DbHistorico(Model):
    __database__ = db
    id = AutoIncrementField(primary_key=True)
    nome_usuario=TextField(default='0', index=True,fts=True)
    acao=TextField(default='0',index=True)
    momento=DateTimeField(default=datetime.datetime.now,index=True)
    parametros_funcao=HashField()

    def create_historico(self, **kwargs):
        return self.create(**kwargs)

    def hist_dados_cadastrado(self,hist_id,key_value):
        hist_atual=self.load(hist_id)
        for k,v in key_value.items():
            if k =='no_repeat':
                pass
            else:
                hist_atual.parametros_funcao[k]=v
        hist_atual.save()

    def ver_dados_cadastrados(self,id_hist):
        historico=self.load(id_hist)

        dados= dict()
        for x,y in historico.parametros_funcao.items():
            dados[x.decode('UTF-8')]=y.decode('UTF-8')

        return dados

    def read_historico(self):
        historico = []
        for search in DbHistorico.query(order_by=DbHistorico.id):
            historico.append(
                dict(
                    id=search.id, nome_usuario=search.nome_usuario,acao=search.acao,momento=search.momento
                )
            )

        return reversed(historico)

    def update_historico(self,**kwargs):
        '''
        Em progresso , mas servira basicamente para armazenar os dados de criaçao e modificaçao de tudo.
        :param kwargs:
        :return:
        '''
        new_data_historico = kwargs['historico']
        estrutura = self.load(int(new_data_historico['id']))
        for i in new_data_historico:
            if new_data_historico[i] and new_data_historico[i] != ' ':
                setattr(estrutura, i, new_data_historico[i])
        if estrutura.save():
            return True
        else:
            return False

    def search_historico_id(self,id):
        if id != '0':
            lista = DbHistorico.load(int(id))
            lista_dic = vars(lista)["_data"]
        else:
            lista_dic = -1

        return lista_dic
    def search_historico_nome(self, nome):
        listas = []

        for lista in DbHistorico.query((DbHistorico.nome_usuario == nome),
                                       order_by=DbHistorico.id):
            listas.append(vars(lista)["_data"])

        return listas

    def search_historico_acao(self,acao):
        listas = []

        for lista in DbHistorico.query((DbHistorico.acao == acao),
                                       order_by=DbHistorico.id):
            listas.append(vars(lista)["_data"])

        return listas