# encoding: utf-8

from model.aluno_model import DbAluno


class AlunoFacade:

    def __init__(self):
        self.aluno = DbAluno()


    def create_aluno_facade(self, **kwargs:str):
        return self.aluno.create_aluno(**kwargs)

    def read_aluno_facade(self):
        return self.aluno.read_aluno()

    def update_aluno_facade(self, id:int, nome:str,nome_login:str,turma):
        return self.aluno.update_aluno(update_id=id, nome=nome,nome_login=nome_login,vinculo_turma=turma)

    def set_itens_student_facade(self, id, itens):
        return self.aluno.set_itens_student(id, itens)

    def get_itens_student_facade(self,id):
        return self.aluno.get_itens_student(id=id)

    def delete_aluno_facade(self, deletar_ids:list):
        return self.aluno.aluno_delete(deletar_ids)

    def search_aluno_primeiro_nome_facade(self, primeiro_nome:str):
        return self.aluno.search_aluno_primeiro_nome(primeiro_nome=primeiro_nome)

    def search_aluno_id_facade(self,id_aluno : int):
        return self.aluno.search_aluno_id(id_aluno=id_aluno)

    def set_apelido_facade(self, id, apelido):
        return self.aluno.set_apelido(id=id, apelido=apelido)

    def search_aluno_escola_facade(self, vinculo_escola: int):
        return self.aluno.search_aluno_by_escola(escola=vinculo_escola)


    def search_aluno_nome_facade(self, nome:str):
        return self.aluno.search_aluno_nome(nome)


    def search_aluno_nome_login_facade(self, nome_login:str):
        return self.aluno.search_aluno_nome_login(nome_login)


    def search_aluno_nome_objeto_facade(self, nome:str):
        return self.aluno.pesquisa_aluno_objeto(nome)


    def aluno_in_turma_facade(self, id_aluno:list, vinculo_turma:str):
        return self.aluno.alunos_in_turma(id_aluno=id_aluno, vinculo_turma=vinculo_turma)


    def compra_item_facade(self, id_usuario:int, id_item:int):
        return self.aluno.comprar_item(id_usuario=id_usuario, id_item=id_item)


    def ver_item_comprado_facade(self, id_usuario:int):
        return self.aluno.ver_itens_comprados(id_usuario)


    def equipar_item_facade(self, id:int, itens:list):
        return self.aluno.equipar_item(id_usuario=id, itens=itens)


    def avatar_facade(self, id:int):
        return self.aluno.avatar(id)


    def anotacoes_aluno_facade(self, usuario_id:int, mensagem:str):
        return self.aluno.anotacoes_do_aluno(usuario_id, mensagem)


    def read_anotacoes_aluno_facade(self, usuario_id:int):
        return self.aluno.ver_anotacoes_aluno(usuario_id)


    def search_aluno_by_rede_facade(self, vinculo_rede:str):
        return self.aluno.search_aluno_by_rede(vinculo_rede=vinculo_rede)


    def search_aluno_by_turma_facade(self, vinculo_turma:str):
        return self.aluno.search_aluno_by_turma(vinculo_turma=vinculo_turma)

    def gravar_premiacao(self,user_id,premiacao):
        return self.aluno.gravar_premiacao(user_id,premiacao)

    def armazenar_ultimo_jogo_jogado(self, id_aluno, jogo):
        return self.aluno.armazenar_ultimo_jogo_jogado(id_aluno, jogo)

    def ultimo_oa_jogado_facade(self, id_aluno):
        return self.aluno.mostrar_ultimo_oa_jogado(id_aluno)

    def mostrar_ultimo_oa_jogado(self,id_aluno):
        return self.aluno.mostrar_ultimo_oa_jogado(id_aluno)

    def set_medalha_facade(self, id_aluno, medalha, motivo):
        return self.aluno.set_medalha(id_aluno=id_aluno, medalha=medalha, motivo=motivo)

    def get_medalhas_facade(self, id_aluno):
        return self.aluno.get_medalhas(id_aluno=id_aluno)

    def vincular_responsavel_facade(self, id_aluno, id_responsavel):
        return self.aluno.vincular_responsavel(id_aluno=id_aluno, id_responsavel=id_responsavel)

    def get_alunos_sem_responsaveis_facade(self, vinculo_rede=None, vinculo_escola=None, vinculo_turma=None):
        return self.aluno.get_alunos_sem_responsaveis(vinculo_rede=vinculo_rede, vinculo_escola=vinculo_escola, vinculo_turma=vinculo_turma)

    def get_alunos_viculo_responsavel_facade(self, id_responsavel):
        return self.aluno.get_alunos_viculo_responsavel(id_responsavel=id_responsavel)

    def apagartudo(self):
        return self.aluno.apagartudo()

