# encoding: utf-8

from walrus import *
from random import randrange

db = Database(host='localhost', port=6379, db=0)


class DbAluno(Model):
    __database__ = db
    id = AutoIncrementField(primary_key=True)
    matricula = TextField()
    nome = TextField(fts=True, index=True)
    primeiro_nome = TextField(fts=True, index=True)
    nascimento = TextField(fts=True)
    sexo = TextField(fts=True)
    nome_login = TextField(fts=True)
    senha = TextField()
    email = TextField(default='0')
    tipo_aluno = TextField(default='0')
    cpf_responsavel = TextField(default='0')
    apelido = TextField(fts=True, default='0')

    armario = ListField()
    cor = TextField(default='0')
    rosto = TextField(default='0')
    acessorio = TextField(default='0')
    corpo = TextField(default='0')

    pontos_de_vida = TextField(fts=True,default='0')
    pontos_de_moedas = TextField(fts=True,default='0')
    medalhas = ListField()

    vinculo_rede = TextField(fts=True, default='0')
    vinculo_escola = TextField(fts=True, default='0')
    vinculo_turma = TextField(fts=True, index=True, default='0')
    vinculo_serie = TextField(fts=True, default='0')
    vinculo_responsavel = TextField(fts=True, default='0')

    ultimo_oa_jogado=TextField(fts=True,default='0')
    ultima_aventura = TextField(fts=True, default='0')
    ultima_unidade = TextField(fts=True, default='0')
    ultima_objeto_aprendizagem = TextField(fts=True, default='0')
    anotacoes_aluno = ListField()
    dados_aventura_1 = HashField()
    dados_aventura_2 = HashField()
    dados_aventura_3 = HashField()


    def create_aluno(self, **kwargs):
        return self.create(**kwargs)


    def update_aluno(self, update_id, nome, nome_login, vinculo_turma='0', escola='0', rede='0'):
        print('update_aluno',vinculo_turma)
        aluno_up = self.load(update_id)
        [setattr(aluno_up, parametro, valor) for parametro, valor in locals().items() if
         valor != aluno_up.all()]
        aluno_up.save()

    def read_aluno(self):
        # O administrador deveria ver tambem a senha do aluno , lembrete de modificar esse metodo
        alunos = []
        for search in DbAluno.query(order_by=DbAluno.nome):
            alunos.append(
                dict(
                    id=search.id, matricula=search.matricula, nome=search.nome, senha=search.senha,
                    tipo=search.tipo_aluno, cor=search.cor,armario=search.armario, rosto=search.rosto,
                    acessorio=search.acessorio, corpo=search.corpo,pontos_de_vida=search.pontos_de_vida,
                    pontos_de_moedas=search.pontos_de_moedas, vinculo_escola=search.vinculo_escola, vinculo_rede=search.vinculo_rede,
                    vinculo_turma=search.vinculo_turma, email=search.email, cpf='', nome_login=search.nome_login,
                    nascimento=search.nascimento
                )
            )
        return alunos

    def set_itens_student(self, id, itens):
        student = DbAluno.load(int(id))
        try:
            for i in itens:
                student.armario.append(i['id'])
            student.save()

            return True
        except:
            return False

    def get_itens_student(self, id):
        student_itens = DbAluno.load(int(id))
        return student_itens.armario

    def search_aluno_primeiro_nome(self, primeiro_nome):
        alun_pes = []
        for search in DbAluno.query(DbAluno.primeiro_nome == primeiro_nome):
            alun_pes.append(vars(search)["_data"])

        return alun_pes

    def search_aluno_nome_login(self, nome_login):

        alun_pes = None
        for search in DbAluno.query(DbAluno.nome_login == nome_login):
            alun_pes = vars(search)['_data']
            alun_pes['tipo'] = alun_pes['tipo_aluno']

        return alun_pes

    def get_itens_closet(self):
        pass

    def search_aluno_nome(self, nome):

        alun_pes = []
        for search in DbAluno.query((DbAluno.nome == nome), order_by=self.id):
            alun_pes = vars(search)["_data"]

        return alun_pes


    def search_aluno_by_rede(self, vinculo_rede):
        alunos = []
        for search in DbAluno.query((DbAluno.vinculo_rede == vinculo_rede), order_by=DbAluno.nome):
            alunos.append(
                dict(
                    id=search.id, matricula=search.matricula, nome=search.nome, senha=search.senha,
                    tipo=search.tipo_aluno, cor=search.cor,
                    rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                    pontos_de_vida=search.pontos_de_vida, pontos_de_moedas=search.pontos_de_moedas,
                    vinculo_escola=search.vinculo_escola, vinculo_rede=search.vinculo_rede,
                    vinculo_turma=search.vinculo_turma, email=search.email, cpf='', nascimento = search.nascimento,
                    nome_login= search.nome_login
                )
            )
        return alunos

    def search_aluno_by_escola(self, escola):
        alunos = []

        for search in DbAluno.query((DbAluno.vinculo_escola == escola), order_by=DbAluno.nome):
            alunos.append(
                dict(
                    id=search.id, matricula=search.matricula, nome=search.nome, senha=search.senha,
                    tipo=search.tipo_aluno, cor=search.cor,
                    rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                    pontos_de_vida=search.pontos_de_vida, pontos_de_moedas=search.pontos_de_moedas,
                    vinculo_escola=search.vinculo_escola, vinculo_rede=search.vinculo_rede,
                    vinculo_turma=search.vinculo_turma, email=search.email, cpf='', nascimento = search.nascimento,
                    nome_login=search.nome_login
                )
            )

        return alunos

    def search_aluno_by_turma(self, vinculo_turma):
        alunos = []
        for search in DbAluno.query((DbAluno.vinculo_turma == vinculo_turma), order_by=DbAluno.nome):
            alunos.append(
                dict(
                    id=search.id, matricula=search.matricula, nome=search.nome, senha=search.senha,
                    tipo=search.tipo_aluno, armario=search.armario, cor=search.cor, medalha = [''.join(str(i.decode('utf-8'))) for i in search.medalhas],
                    rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                    pontos_de_vida=search.pontos_de_vida, pontos_de_moedas=search.pontos_de_moedas,
                    vinculo_escola=search.vinculo_escola, vinculo_rede=search.vinculo_rede,
                    vinculo_turma=search.vinculo_turma, email=search.email, cpf='', nome_login=search.nome_login,
                    nascimento=search.nascimento
                )
            )
        return alunos

    def search_aluno_by_serie(self,vinculo_serie):
        alunos = []
        for search in DbAluno.query(DbAluno.vinculo_serie== vinculo_serie,order_by=DbAluno.nome):
            alunos.append(
                dict(
                    id=search.id, matricula=search.matricula, nome=search.nome, senha=search.senha,
                    tipo=search.tipo_aluno, itens_comprados=search.itens_comprados, cor=search.cor,
                    rosto=search.rosto, acessorio=search.acessorio, corpo=search.corpo,
                    pontos_de_vida=search.pontos_de_vida, pontos_de_moedas=search.pontos_de_moedas,
                    vinculo_escola=search.vinculo_escola, vinculo_rede=search.vinculo_rede,
                    vinculo_turma=search.vinculo_turma, email=search.email, cpf=''
                )
            )
            return alunos

    def pesquisa_aluno_objeto(self, nome_aluno):

    # pesquisa aluno esta retornando o objeto em sua totalidade , NAO DELETAR ESSE METODO  , pois é usado em Dbcemiterio

        aluno_pes = []
        for pesquisa in DbAluno.query(DbAluno.nome == nome_aluno):
            aluno_pes = pesquisa

        return aluno_pes

    def search_aluno_id(self,id_aluno):

        aluno = DbAluno.load(int(id_aluno))
        alun_pes = vars(aluno)["_data"]
        alun_pes['medalha'] = aluno.medalhas

        return alun_pes

    def set_apelido(self, id, apelido):
        aluno = DbAluno.load(int(id))
        aluno.apelido = apelido
        aluno.save()

    def alunos_in_turma(self, id_aluno, vinculo_turma):
        from facade.estrutura_facade import EstruturaFacade
        facade = EstruturaFacade()
        turmi = facade.search_estrutura_id_facade(vinculo_turma)


        for id_aluno in id_aluno:
            aluno = self.load(int(id_aluno))
            aluno.vinculo_turma = str(vinculo_turma)
            aluno.vinculo_serie = turmi['serie']
            aluno.save()

    def comprar_item(self, id_usuario, id_item):
        from model.estrutura_model import DbEstrutura

        item = DbEstrutura()
        usuario = DbAluno.load(id_usuario)
        preco = item.search_estrutura_id(id_item)['preco']
        if int(usuario.pontos_de_moedas) >= int(preco):
            dinheiros = int(usuario.pontos_de_moedas)
            dinheiros -= int(preco)
            usuario.pontos_de_moedas = str(dinheiros)
            usuario.armario.append(id_item)
            usuario.save()
            return True
        else:
            print("você não tem moeda")
            return False

    def ver_itens_comprados(self, id_usuario):
        #         id_usuario
        # id_usuario=usuario_logado()
        usuario = DbAluno.load(id_usuario)
        itens = [''.join(str(x.decode('utf-8'))) for x in usuario.itens_comprados]
        return itens

    def equipar_item(self, id_usuario, itens):
        usuario = self.load(id_usuario)
        for i in itens:
           if i != -1:
                if i['tipo_item'] == '1':
                    usuario.cor = i['id']
                elif i['tipo_item'] == '2':
                    usuario.rosto = i['id']
                elif i['tipo_item'] == '3':
                    usuario.acessorio = i['id']
                elif i['tipo_item'] == '4':
                    usuario.corpo = i['id']
        usuario.save()



    def avatar(self, id):

        aluno_av = self.load(id)
        return dict(cor=aluno_av.cor, rosto=aluno_av.rosto, acessorio=aluno_av.acessorio, corpo=aluno_av.corpo)

    def anotacoes_do_aluno(self, id_usuario, mensagem):
        aluno_anot = self.load(id_usuario)
        aluno_anot.anotacoes_aluno.append(mensagem)
        aluno_anot.save()

    def ver_anotacoes_aluno(self, id_aluno):
        aluno_re_anot = self.load(id_aluno)
        anotacoes = []
        for x in aluno_re_anot.anotacoes_aluno:
            anotacoes.append(x.decode('utf-8'))

        return anotacoes

    def aluno_delete(self, deletar_ids):

        for deletar_ids in deletar_ids:
            usuario = self.load(deletar_ids)
            usuario.delete(deletar_ids)

    def gravar_premiacao(self,user_id,premio):

        aluno =self.load(int(user_id))
        moedas=int(aluno.pontos_de_moedas)
        vidas=int(aluno.pontos_de_vida)
        moedas+= int(premio['moedas'])
        vidas +=int(premio['xp'])
        if premio['medalhas'] != [] or premio['medalhas'] != None or premio['medalhas'] != False:
            for i in premio['medalhas']:
                aluno.medalhas.append(dict(id_medalha=i, motivo_medalha=""))
        aluno.pontos_de_moedas=str(moedas)
        aluno.pontos_de_vida=str(vidas)
        aluno.save()

    def armazenar_ultimo_jogo_jogado(self, id_aluno, jogo):
        aluno=self.load(id_aluno)
        aluno.ultimo_oa_jogado=jogo
        aluno.save()

    def mostrar_ultimo_oa_jogado(self,id_aluno):
        aluno=self.search_aluno_id(id_aluno)

        return aluno['ultimo_oa_jogado']

    def set_medalha(self, id_aluno, medalha, motivo):
        try:
            aluno = DbAluno.load(int(id_aluno))
            aluno.medalhas.append(dict(id_medalha=medalha, motivo_medalha=motivo))
        except KeyError:

            return False
        else:
            aluno.save()
            return True

    def get_medalhas(self, id_aluno):

        aluno=DbAluno.load(int(id_aluno))

        return aluno.medalhas

    def vincular_responsavel(self, id_aluno, id_responsavel):
        aluno = DbAluno.load(int(id_aluno))
        aluno.vinculo_responsavel = str(id_responsavel)
        aluno.save()

        return aluno

    def get_alunos_sem_responsaveis(self, vinculo_rede, vinculo_escola, vinculo_turma):
        aluno = []
        if vinculo_rede:
            for i in DbAluno.query((DbAluno.vinculo_rede == vinculo_rede) & (DbAluno.vinculo_responsavel == '0'),
                                   order_by=DbAluno.nome):
                aluno.append(vars(i)["_data"])
        elif vinculo_escola:
            for i in DbAluno.query((DbAluno.vinculo_escola == vinculo_escola) & (DbAluno.vinculo_responsavel == '0'),
                                   order_by=DbAluno.nome):
                aluno.append(vars(i)["_data"])
        elif vinculo_turma:
            for i in DbAluno.query((DbAluno.vinculo_turma == vinculo_turma) & (DbAluno.vinculo_responsavel == '0'),
                                   order_by=DbAluno.nome):
                aluno.append(vars(i)["_data"])
        else:
            for i in DbAluno.query((DbAluno.vinculo_responsavel == '0'), order_by=DbAluno.nome):
                aluno.append(vars(i)["_data"])

        return aluno

    def get_alunos_viculo_responsavel(self, id_responsavel):
        aluno = []

        for i in DbAluno.query((DbAluno.vinculo_responsavel == id_responsavel), order_by=DbAluno.nome):
            aluno.append(vars(i)["_data"])

        return aluno

    def apagartudo(self):
        db.flushall()
