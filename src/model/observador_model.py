# encoding: utf-8

from walrus import *
from datetime import date

db = Database(host='localhost', port=6379, db=0)


class DbObservador(Model):
    __database__ = db

    id = AutoIncrementField(primary_key=True)
    nome = TextField(fts=True, index=True)
    senha = TextField(default='0')
    telefone = TextField(default='0')
    cpf = TextField(default='0')
    email = TextField(fts=True,default='0')
    data_nascimento=TextField(fts=True, default='0')
    tipo = TextField(fts=True)
    nome_foto_perfil=TextField(default='default-profile.png')
    apelido = TextField(fts=True, default='0')
    armario = ListField()
    cor = TextField(default='0')
    rosto = TextField(default='0')
    acessorio = TextField(default='0')
    corpo = TextField(default='0')

    vinculo_rede = TextField(fts=True, default='0')
    vinculo_escola = TextField(fts=True, default='0')
    vinculo_turma = TextField(fts=True, default='0')

    pontos_de_vida = IntegerField(default=0)
    pontos_de_moedas = IntegerField(default=0)

    data_ultimo_login = TextField(default='',index=True)
    ativo = TextField(default='0')
    aux_css_foto=TextField(default='0')



    def create_observador(self, **kwargs):
        return self.create(**kwargs)

    def read_observador(self):

        observador = []
        for search in DbObservador.all():
            observador.append(
                dict(
                    id=search.id, nome=search.nome, senha=search.senha, telefone=search.telefone,
                    cpf=search.cpf, email=search.email, tipo=search.tipo,
                    cor=search.cor, rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                    vida=search.pontos_de_vida, moedas=search.pontos_de_moedas, vinculo_escola=search.vinculo_escola,
                    nascimento=search.data_nascimento, vinculo_rede=search.vinculo_rede, vinculo_turma=search.vinculo_turma
                )
            )

        return observador

    def update_observador(self, **kwargs):

        observador = self.load(kwargs['id'])
        for i in kwargs:
            if kwargs[i] and kwargs[i] != ' ':
                setattr(observador, i, kwargs[i])
        if observador.save():
            return True
        else:
            return False
        # [setattr(observador, parametro, valor) for parametro, valor in locals().items() if valor !=observador.all()]
        # observador.save()

    def redefinir_senha(self, id, senha):
        observador = DbObservador.load(id)
        observador.senha = senha
        observador.ativo = '1'

        observador.save()

    def get_itens_responsaveis(self, id):
        responsaveis_itens = DbObservador.load(int(id))
        return responsaveis_itens.armario

    def set_itens_responsaveis(self, id, itens):
        student = DbObservador.load(int(id))
        try:
            for i in itens:
                student.armario.append(i['id'])
            student.save()

            return True
        except:
            return False

    def search_observador_id(self, id):

        observador = self.load(id)
        retorno = vars(observador)["_data"]

        return retorno

    def search_observador_email(self, email):
        observador = None
        for search in DbObservador.query((DbObservador.email == email)):
            observador = dict(id=search.id, nome=search.nome, senha=search.senha, telefone=search.telefone,
                              cpf=search.cpf, email=search.email, tipo=search.tipo,
                              vinculo_escola=search.vinculo_escola,
                              vinculo_rede=search.vinculo_rede, vinculo_turma=search.vinculo_turma)

        return observador

    def search_observador(self, nome):
        """
        procura o observador e coloca os dados em uma entrada de dicionario
        :param nome: nome do observador
        :return:
        """
        observador = None
        for search in DbObservador.query(DbObservador.nome == nome):
            observador = dict(
                id=search.id, nome=search.nome, senha=search.senha, telefone=search.telefone,
                cpf=search.cpf, email=search.email, tipo=search.tipo,
                cor=search.cor, rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                vida=search.pontos_de_vida, moedas=search.pontos_de_moedas, vinculo_escola=search.vinculo_escola,
                vinculo_rede=search.vinculo_rede, vinculo_turma=search.vinculo_turma
            )

        return observador

    def search_observador_tipo(self, tipo):
        """
        procura o observador e coloca os dados em uma entrada de dicionario
        :param nome: nome do observador
        :return:
        """
        observador = []
        for search in DbObservador.query(DbObservador.tipo == tipo, order_by=DbObservador.nome):
            observador.append(dict(
                    id=search.id, nome=search.nome, senha=search.senha, telefone=search.telefone,
                    cpf=search.cpf, email=search.email, tipo=search.tipo,
                    cor=search.cor, rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                    vida=search.pontos_de_vida, moedas=search.pontos_de_moedas, vinculo_escola=search.vinculo_escola,
                    vinculo_rede=search.vinculo_rede, vinculo_turma=search.vinculo_turma
                )
            )

        return observador

    def search_observador_tipo_nome(self,tipo,nome):
        lista_dic = None
        for search in DbObservador.query((DbObservador.tipo == tipo and DbObservador.nome == nome)):
            lista_dic = dict(id=search.id, nome=search.nome, senha=search.senha, telefone=search.telefone,
                                   cpf=search.cpf, email=search.email, tipo=search.tipo,
                                   vinculo_escola=search.vinculo_escola,vinculo_turma=search.vinculo_turma,
                                   vinculo_rede=search.vinculo_rede)
        return lista_dic

    def search_observador_escola(self,vinculo_escola):
        observador = []
        for search in DbObservador.query((DbObservador.vinculo_escola == vinculo_escola), order_by=DbObservador.nome):
            observador.append(
                dict(
                    id=search.id, nome=search.nome, senha=search.senha, telefone=search.telefone,
                    cpf=search.cpf, email=search.email, tipo=search.tipo,
                    cor=search.cor, rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                    vida=search.pontos_de_vida, moedas=search.pontos_de_moedas, vinculo_escola=search.vinculo_escola,
                    vinculo_rede=search.vinculo_rede, vinculo_turma=search.vinculo_turma, nascimento=search.data_nascimento
                )
            )
        return observador


    def search_observador_turma(self, vinculo_turma):
        observador = []
        for search in DbObservador.query((DbObservador.vinculo_turma == vinculo_turma), order_by=DbObservador.nome):
            observador.append(
                dict(
                    id=search.id, nome=search.nome, senha=search.senha, telefone=search.telefone,
                    cpf=search.cpf, email=search.email, tipo=search.tipo, itens_comprados=search.armario,
                    cor=search.cor, rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                    vida=search.pontos_de_vida, moedas=search.pontos_de_moedas, vinculo_escola=search.vinculo_escola,
                    vinculo_rede=search.vinculo_rede, vinculo_turma=search.vinculo_turma
                )
            )

        return observador

    def search_observador_rede(self, vinculo_rede):
        observador = []
        for read in DbObservador.query(DbObservador.vinculo_rede == vinculo_rede, order_by=DbObservador.nome):
            observador.append(dict(id=read.id, nome=read.nome, senha=read.senha, telefone=read.telefone, cpf=read.cpf,
                     email=read.email, tipo=read.tipo, vinculo_rede=read.vinculo_rede, vinculo_escola=read.vinculo_escola,
                     vinculo_turma=read.vinculo_turma, nascimento=read.data_nascimento))


        return observador

    def search_observador_inativos(self, nome_observador):
        usuario = []
        for pesquisa in DbObservador.query(DbObservador.nome == nome_observador):
            usuario = pesquisa

        return usuario

    def search_diretor_vinculo_escola(self, vinculo_escola):
        from control.dicionarios import TIPO_USUARIOS
        observador = None
        for search in DbObservador.query((DbObservador.tipo == TIPO_USUARIOS['diretor']) & (DbObservador.vinculo_escola == vinculo_escola)):
            observador = vars(search)["_data"]

        return observador


    def login_date(self, id, data):
        """
        Armazena o historico de login
        :param id: id do usuario que logou
        :param data: data , hora e minutos do login
        :return:
        """
        observador = self.load(id)
        observador.data_login = data
        observador.save()

    def observador_in_turma(self, id_observador, vinculo_turma):

        for id_observador in id_observador:
            observador = self.load(int(id_observador))
            observador.vinculo_turma = str(vinculo_turma)
            observador.save()


    def delete_observador(self, deletar_ids):
        for deletar_ids in deletar_ids:
            usuario = self.load(deletar_ids)
            usuario.delete(deletar_ids)

    def equipar_item(self, id_usuario, itens):

        usuario = self.load(id_usuario)
        if itens['tipo_item'] == '1':
            usuario.cor = itens['id']
        else:
            if itens['tipo_item'] == '2':
                usuario.rosto = itens['id']
            else:
                if itens['tipo_item'] == '3':
                    usuario.acessorio = itens['id']
                else:
                    if itens['tipo_item'] == '4':
                        usuario.corpo = itens['id']
        usuario.save()

    def pesquisa_email(self, letras):
        observador = []
        for i in DbObservador.all():
            if letras in i.email:
                observador.append(vars(i)["_data"])

        return observador