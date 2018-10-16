# encoding: utf-8

from walrus import *
from control.dicionarios import TIPO_ESTRUTURA

db = Database(host='localhost', port=6379, db=0)


class DbEstrutura(Model):
    __database__ = db
    id = AutoIncrementField(primary_key=True)
    nome = TextField(index=True)
    tipo_estrutura = TextField(fts=True, index=True)
    telefone = TextField(default='0')

    vinculo_rede = TextField(fts=True, default='0')
    vinculo_escola = TextField(fts=True, default='0')
    vinculo_diretor_escola = TextField(fts=True, default='0')
    vinculo_professor_turma = TextField(fts=True, default='0')
    vinculo_professor2_turma = TextField(fts=True, default='0')
    cnpj = TextField(default='0')

    endereco = TextField(default='0',index=True,fts=True)
    numero = TextField(default='0',index=True,fts=True)
    bairro = TextField(default='0',index=True,fts=True)
    complemento = TextField(default='0',index=True,fts=True)
    cep = TextField(default='0',index=True,fts=True)
    estado = TextField(default='0',index=True,fts=True)
    municipio = TextField(default='0',index=True,fts=True)

    sigla_oa = TextField(fts=True, default='0')
    unidade=TextField(fts=True, default='0')

    tipo_oa=TextField(fts=True, default='0')

    sigla_descritor = TextField(fts=True, default='0')
    nome_descritor = TextField(fts=True, default='0')
    descricao_descritor = TextField(fts=True, default='0')

    disciplina = TextField(fts=True, default='0')
    aventura = TextField(fts=True, default='0')

    quem_criou = TextField(default='0')
    data_de_criacao = TextField(default='0')
    serie = TextField(fts=True, default='0')

    tipo_item = TextField(fts=True, default='0')
    preco = TextField(fts=True, default='0')
    image_name = TextField(fts=True, default="0")


    tipo_medalha = TextField(default='0')
    descricao = TextField(default='0')
    descricao_completa = TextField(default='0')

    nome_usuario = TextField(default='0')
    tipo_usuario = TextField(default='0')
    data_acesso = DateTimeField(default=datetime.datetime.now)

    anotacoes_observador_turma = ListField()
    anotacoes_observador_escola = ListField()
    anotacoes_observador_rede = ListField()

    ativo = TextField(fts = True,default = '1')

    def create_estrutura(self, **kwargs):
        return self.create(**kwargs)

    def read_estrutura(self, tipo_estrutura):
        listas = []

        for lista in DbEstrutura.query((DbEstrutura.tipo_estrutura == tipo_estrutura) & (DbEstrutura.ativo == '1'), order_by=DbEstrutura.id):
            listas.append(vars(lista)["_data"])

        return listas

    # def ja_possui_item(self, usuario_logado):
    #     from model.aluno_model import DbAluno
    #
    #     usuario = DbAluno()
    #     # [x.decode('utf-8') for x in usuario.i]
    #     itens_usuario = usuario.ver_itens_comprados(id_usuario=int(usuario_logado))
    #     itens = [str(y['id']) for y in self.read_estrutura(tipo_estrutura=TIPO_ESTRUTURA['item'])]
    #     lista_teste = [z for z in itens if z not in itens_usuario]
    #     return lista_teste

    def search_estrutura(self, tipo_estrutura, nome):
        lista_dic= []
        for lista in DbEstrutura.query(DbEstrutura.tipo_estrutura == tipo_estrutura and DbEstrutura.nome == nome):
            lista_dic=vars(lista)["_data"]

        return lista_dic

    def search_estrutura_id(self, id):
        if id != '0':
            lista = DbEstrutura.load(int(id))
            lista_dic = vars(lista)["_data"]
        else:
            lista_dic = -1

        return lista_dic

    def search_escola_by_rede(self, vinculo_rede):
        escola = []
        for lista in DbEstrutura.query((DbEstrutura.tipo_estrutura == '2') & (DbEstrutura.vinculo_rede == vinculo_rede) &
                                       (DbEstrutura.ativo == '1'),order_by=self.nome):
            escola.append(vars(lista)["_data"])

        return escola

    def search_turma_by_rede(self, vinculo_rede):
        turma = []
        for lista in self.query((DbEstrutura.tipo_estrutura == '3') & (DbEstrutura.vinculo_rede == vinculo_rede),
                                order_by=DbEstrutura.nome):
            turma.append(vars(lista)["_data"])

        return turma

    def search_turma_by_escola(self, vinculo_escola):
        turma = []
        for lista in self.query((DbEstrutura.tipo_estrutura == '3') & (DbEstrutura.vinculo_escola == vinculo_escola),
                                order_by=DbEstrutura.nome):
            turma.append(vars(lista)["_data"])

        return turma

    def search_descritor_serie(self,serie):
        from control.dicionarios import TIPO_ESTRUTURA
        oas = []

        for i in DbEstrutura.query((DbEstrutura.tipo_estrutura == TIPO_ESTRUTURA['objeto_de_aprendizagem']) &
                                   (DbEstrutura.serie == serie), order_by=DbEstrutura.id):

            oas.append(vars(i)["_data"])

        return oas

    def search_descritor_serie_diciplina(self,serie, diciplina):
        from control.dicionarios import TIPO_ESTRUTURA, DICIPLINA_NOME

        oas = []

        for i in DbEstrutura.query((DbEstrutura.tipo_estrutura == TIPO_ESTRUTURA['objeto_de_aprendizagem']) &
                                   (DbEstrutura.serie == serie) & (DbEstrutura.disciplina == diciplina), order_by=DbEstrutura.id):

            oas.append(vars(i)["_data"])

        return oas

    def search_oa_by_type_and_aventura(self, aventura ,disciplina):
        oas = []
        for i in self.query((DbEstrutura.tipo_estrutura == '7') & (DbEstrutura.disciplina == disciplina) &
                            (DbEstrutura.aventura == aventura), order_by=DbEstrutura.sigla_oa):
            oas.append(vars(i)["_data"])

        return oas

    def get_itens_free(self):
        itens = []
        for i in DbEstrutura.query((DbEstrutura.tipo_estrutura == '4') & (DbEstrutura.preco == '0'), order_by=DbEstrutura.id):
            itens.append(vars(i)["_data"])

        return itens


    def get_itens_for_type(self, type_item):
        itens = []
        for i in DbEstrutura.query((DbEstrutura.tipo_item == type_item), order_by=DbEstrutura.id):
            itens.append(vars(i)["_data"])

        return itens


    def update_estrutura(self, **kwargs:dict):
        new_data_estrutura = kwargs['estrutura']
        estrutura = self.load(int(new_data_estrutura['id']))
        for i in new_data_estrutura:
            if new_data_estrutura[i] and new_data_estrutura[i] != ' ':
                setattr(estrutura, i, new_data_estrutura[i])
        if estrutura.save():
            return True
        else:
            return False

    def delete_estrutura(self, id):
        estrutura = self.load(int(id))
        estrutura.ativo = '0'
        estrutura.save()

    # def func_anotacoes_estrutura_turma(self, id_estrutura, mensagem):
    #     estrutura = self.load(id_estrutura)
    #     estrutura.anotacoes_estrutura_turma.append(mensagem)
    #     estrutura.save()
    #
    # def func_anotacoes_estrutura_escola(self, id_estrutura, mensagem):
    #     estrutura = self.load(id_estrutura)
    #     estrutura.anotacoes_estrutura_escola.append(mensagem)
    #     estrutura.save()
    #
    # def func_anotacoes_estrutura_rede(self, id_estrutura, mensagem):
    #     estrutura = self.load(id_estrutura)
    #     estrutura.anotacoes_estrutura_rede.append(mensagem)
    #     estrutura.save()
