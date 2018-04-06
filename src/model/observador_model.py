from walrus import *

db = Database(host='localhost', port=6379, db=0)


class DbObservador(Model):
    __database__ = db
    id = AutoIncrementField(primary_key=True)
    nome = TextField(fts=True)
    senha = TextField()
    telefone = TextField()
    cpf = TextField()
    email = TextField()
    tipo = TextField()
    data_ultimo_login = TextField()

    def create_observador(self, nome, senha, telefone, cpf, email, tipo):
        """
        cria um observador
        :param nome: nome do observador
        :param senha: senha
        :param telefone: telefone do usuario(opcional)
        :param cpf: cpf(opcional)
        :param email: email
        :param tipo: o tipo de observador , professor , responsave, diretor , gestor ou administrador
        :return: true se criou certinho e false se n deu certo
        """
        if self.create(nome=nome, senha=senha, telefone=telefone, cpf=cpf, email=email, tipo=tipo):
            return True
        else:
            return False

    def read_observador(self):
        """
        coloca os dados do observador em um dicionario
        :return: o dicionario com os dados
        """
        observador = []
        for read in DbObservador.all():
            observador.append(dict(id=read.id, nome=read.nome, senha=read.senha, telefone=read.telefone, cpf=read.cpf,
                                   email=read.email, tipo=read.tipo))

        return observador

    def update_observador(self, id, nome, telefone, cpf, email):
        """
        edita o observador
        :param id: id do observador a ser editado
        :param nome: novo nome
        :param telefone: novo telefone
        :param cpf: nvo cpf
        :param email: novo email
        :return:
        """
        observador = DbObservador.load(id)
        observador.nome = nome
        observador.telefone = telefone
        observador.cpf = cpf
        observador.email = email

        observador.save()

    def delete_observador(self, deletar_ids):
        """
        delteta os observadores
        :param deletar_ids: lista de ids de observadores a serem deletados
        :return:
        """
        for deletar_ids in deletar_ids:
            usuario = self.load(deletar_ids)
            usuario.delete(deletar_ids)

    def search_observador(self, nome):
        """
        procura o observador e coloca os dados em uma entrada de dicionario
        :param nome: nome do observador
        :return:
        """

        observador = None
        for search in DbObservador.query(DbObservador.nome == nome):
            observador = dict(id=search.id, nome=search.nome, senha=search.senha, telefone=search.telefone,
                              cpf=search.cpf, email=search.email, tipo=search.tipo)

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


