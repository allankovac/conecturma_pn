# encoding: utf-8

class ValidaNome:
    def __init__(self, proxima_validacao):
        self.proxima_validacao = proxima_validacao

    def validacao(self, nome, senha, telefone, cpf, email, tipo):
        """
        Recebe todos os dados , verifica se o nome recebeu vazio , se n for , avança para o proximo metodo
        Obs: alguns usuarios nao usam esse padrao , entao alguns desses campos tem default None
        :param nome: nome recebido no cadastro
        :param senha: senha recebida no cadastro
        :param telefone: telefone recebido no cadastro
        :param cpf: cpf recebido no cadastro
        :param email: email recebido no cadastro
        :param tipo: tipó recebido no cadastro
        :return:
        """
        if nome == "":
            return False
        else:
            return self.proxima_validacao.validacao(senha, telefone, cpf, email, tipo)


class ValidaSenha:
    def __init__(self, proxima_validacao):

        self.proxima_validacao = proxima_validacao

    def validacao(self, senha, telefone, cpf, email, tipo):
        """Recebe os dados , verifica se a senha recebeu vazio , se n for , avança para o proximo metodo
        :param senha: senha recebida no cadastro
        :param telefone: telefone recebido no cadastro
        :param cpf: cpf recebido no cadastro
        :param email: email recebido no cadastro
        :param tipo: tipó recebido no cadastro
        :return:
        """
        if senha == "":
            return False
        else:
            return self.proxima_validacao.validacao(telefone, cpf, email, tipo)


class ValidaTelefone:
    def __init__(self, proxima_validacao):
        self.proxima_validacao = proxima_validacao

    def validacao(self, telefone, cpf, email, tipo):
        """
        Recebe os dados , verifica se o telefone recebeu vazio , se n for , avança para o proximo metodo
        :param telefone: telefone recebido no cadastro
        :param cpf: cpf recebido no cadastro
        :param email: email recebido no cadastro
        :param tipo: tipó recebido no cadastro
        :return:
              """
        if telefone == "":
            return False
        else:
            return self.proxima_validacao.validacao(cpf, email, tipo)


class ValidaCpf:
    def __init__(self, proxima_validacao):
        self.proxima_validacao = proxima_validacao

    def validacao(self, cpf, email, tipo):
        """
                Recebe os dados , verifica se o telefone  recebeu vazio , se n for , avança para o proximo metodo
                :param cpf: cpf recebido no cadastro
                :param email: email recebido no cadastro
                :param tipo: tipó recebido no cadastro
                :return:
                      """
        if cpf == "":
            return False
        else:
            return self.proxima_validacao.validacao(email, tipo)


class ValidaEmail:
    def __init__(self, proxima_validacao):
        self.proxima_validacao = proxima_validacao

    def validacao(self, email, tipo):
        """
                        Recebe os dados , verifica se o email recebeu vazio , se n for , avança para o proximo metodo
                        :param email: email recebido no cadastro
                        :param tipo: tipó recebido no cadastro
                        :return:
                              """
        if email == "":
            return False
        else:
            return self.proxima_validacao.validacao(tipo)


class ValidaTipo:
    def __init__(self, proxima_validacao):
        self.proxima_validacao = proxima_validacao

    def validacao(self, tipo):
        """
                                Recebe os dados , verifica se o tipo recebeu vazio , se n for , avança para o proximo metodo
                                :param email: email recebido no cadastro
                                :param tipo: tipó recebido no cadastro
                                :return:
                                      """
        if tipo == "":
            return False
        else:
            return self.proxima_validacao.validacao()


class ValidaOk:
    def validacao(self):
        """
        Se a funçao chegar aqui é pq todos os dados que precisam ser preenchidos foram preenchidos
        :return:
        """
        return True
