# coding: utf-8
import unittest
import datetime

from model.estrutura_model import DbEstrutura
from model.historico_model import DbHistorico
from src.facade.facade_main import Facade
from control.dicionarios import TIPO_ESTRUTURA, TIPO_USUARIOS, TIPO_ITEM, TIPO_MEDALHA_NOME, TIPO_OAS_ID

facade = Facade()


class FacadeTest(unittest.TestCase):
    def setUp(self):
        self.facade = Facade()

    """TESTE ALUNO"""

    def _create_aluno(self):

        aluno1 = self.facade.create_aluno_facade(nome="egg", vinculo_escola="Escola Conecturma", matricula="123",
                                                 vinculo_rede="0")
        espero_aluno = self.facade.search_aluno_id_facade(1)
        self.assertIsNotNone(espero_aluno)
        # self.assertEqual(aluno1, True)
        aluno2 = self.facade.create_aluno_facade(nome="dickens silverio", matricula="matri", nome_login="dickens",
                                                 senha="abcd", email="henrique_boladao@bol.com", tipo_aluno="6",
                                                 cpf_responsavel="123594847-42", vinculo_rede="Rede Conecturma",
                                                 vinculo_escola="Escola Conecturma", vinculo_serie="1o ano")
        # self.assertEqual(aluno2, True)
        aluno3 = self.facade.create_aluno_facade(nome='silvio_santos', matricula='23451', nome_login='silvio',
                                                 vinculo_rede="Rede Conecturma", vinculo_turma='KND')
        # self.assertEqual(aluno3, True)
        aluno4 = self.facade.create_aluno_facade(nome='patric_estrela', matricula='23451', nome_login='patrick',
                                                 vinculo_turma='KND')
        # self.assertEqual(aluno4, True)

    def test_create_aluno(self):
        self._create_aluno()

    def _read_aluno(self):
        self._create_aluno()
        for i in range(0, len(self.facade.read_aluno_facade())):
            if self.facade.read_aluno_facade()[i]['id'] == 1:
                self.assertEqual(self.facade.read_aluno_facade()[i]['nome'], 'egg')
            elif self.facade.read_aluno_facade()[i]['id'] == 2:
                self.assertEqual(self.facade.read_aluno_facade()[i]['nome'], 'dickens silverio')
            elif self.facade.read_aluno_facade()[i]['id'] == 3:
                self.assertEqual(self.facade.read_aluno_facade()[i]['nome'], 'silvio_santos')
            elif self.facade.read_aluno_facade()[i]['id'] == 4:
                self.assertEqual(self.facade.read_aluno_facade()[i]['nome'], 'patric_estrela')

    def test_read_aluno(self):
        self._read_aluno()

    def _update_aluno(self):
        self._create_aluno()
        aluno1 = self.facade.search_aluno_nome_facade("dickens silverio")
        self.facade.update_aluno_facade(aluno1['id'], nome="knight", nome_login='KNIGHT',turma='1')
        # self.facade.update_aluno_facade(aluno1['id'], nome="knight", senha="321", turma="do bairro", escola="conectreutrma",
        #                                 rede="de pesca")
        aluno2 = self.facade.search_aluno_nome_facade("knight")
        self.assertEqual(aluno1['id'], aluno2['id'])
        self.assertNotEqual(aluno1['nome'], aluno2['nome'])
        self.assertNotEqual('dickens silverio', aluno2['nome'])
        self.assertNotEqual(aluno1['nome_login'],aluno2['nome_login'])
        self.assertNotEqual(aluno1['vinculo_turma'],aluno2['vinculo_turma'])

    def test_update_aluno(self):
        self._update_aluno()

    def _set_itens_facade(self):
        self._create_estrutura()
        self._create_aluno()

        cabeça=self.facade.search_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'],nome="cabeça")
        ombro= self.facade.search_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'])
        itens=('lista','dicionarios')
        self.facade.set_itens_student_facade('1',)


    def _search_aluno_id_facade(self):
        self._create_aluno()
        aluno = self.facade.search_aluno_id_facade('1')
        self.assertEqual(aluno['nome'], 'egg')
        self.assertEqual(aluno['vinculo_escola'], 'Escola Conecturma')

    def test_pesquisa_aluno_id(self):
        self._search_aluno_id_facade()

    def _search_aluno_escola_facade(self):
        self._create_aluno()
        aluno = self.facade.search_aluno_escola_facade('Escola Conecturma')
        self.assertEqual(aluno[0]['nome'], 'dickens silverio')

    def test_search_aluno_escola(self):
        self._search_aluno_escola_facade()

    def _pesquisa_aluno(self):
        self._create_aluno()
        aluno = self.facade.search_aluno_nome_facade("egg")
        self.assertEqual(aluno['matricula'], '123')
        aluno1 = self.facade.search_aluno_nome_facade("dickens silverio")
        self.assertEqual(aluno1['email'], 'henrique_boladao@bol.com')

    def test_pesquisa_aluno(self):
        self._pesquisa_aluno()

    def _alun_pesquisa_login(self):
        self._create_aluno()
        aluno = self.facade.search_aluno_nome_login_facade('dickens')
        self.assertEqual(aluno['matricula'], 'matri')
        self.assertEqual(aluno['nome'], 'dickens silverio')
        self.assertEqual(aluno['email'], 'henrique_boladao@bol.com')

    def test_pesquisa_login(self):
        self._alun_pesquisa_login()

    def _pesq_alun_obj(self):
        self._create_aluno()
        alun = self.facade.search_aluno_nome_objeto_facade('dickens silverio')
        self.assertIsNotNone(alun.id)
        self.assertIsNotNone(alun.nome)
        self.assertIsNotNone(alun.senha)

    def test_pes_obj_alun(self):
        self._pesq_alun_obj()

    def _aluno_in_turma(self):
        self._create_estrutura()
        aluno1 = self.facade.create_aluno_facade(matricula="0", nome="egg", escola="Escola Conecturma", senha="123",
                                                 vinculo_rede='0')
        alunoer1 = self.facade.search_aluno_nome_facade("egg")
        self.facade.create_aluno_facade(nome="Ni", senha="123", escola="Escola Conecturma", rede="0")
        aluno2 = self.facade.search_aluno_nome_facade("Ni")
        escolhidos = [alunoer1['id'], aluno2['id']]
        turma1 = self.facade.search_estrutura_facade("3", "Knight")
        self.facade.aluno_in_turma_facade(escolhidos, turma1['id'])
        aluntest2 = self.facade.search_aluno_nome_facade('Ni')
        aluntest = self.facade.search_aluno_nome_facade('egg')
        self.assertEqual(aluntest['vinculo_turma'], str(turma1['id']))
        self.assertEqual(aluntest2['vinculo_turma'], str(turma1['id']))

    def test_aluno_in_turma(self):
        self._aluno_in_turma()

    def _anotacoes_no_aluno(self):
        self._create_aluno()
        mensagem2 = "tetativa..."
        mensagem = "Isto é uma mensagem de teste"
        aluno1 = self.facade.search_aluno_nome_objeto_facade("egg")
        self.facade.anotacoes_aluno_facade(aluno1.id, mensagem)
        self.facade.anotacoes_aluno_facade(aluno1.id, mensagem2)
        self.assertEqual(aluno1.anotacoes_aluno[0], mensagem.encode('utf-8'))
        self.assertEqual(aluno1.anotacoes_aluno[1], mensagem2.encode('utf-8'))

    def test_anotacoes_no_aluno(self):
        self._create_aluno()
        self._anotacoes_no_aluno()

    def _read_anotacoes_no_aluno(self):
        self._anotacoes_no_aluno()
        aluno1 = self.facade.search_aluno_nome_facade("egg")
        read = self.facade.read_anotacoes_aluno_facade(aluno1['id'])
        self.assertIn("Isto é uma mensagem de teste", read)

    def test_read_anotacoes_aluno(self):
        self._read_anotacoes_no_aluno()

    def _pes_alun_by_rede(self):
        self._create_aluno()
        alun_rede = self.facade.search_aluno_by_rede_facade('Rede Conecturma')
        self.assertIsNotNone(alun_rede)
        self.assertEqual(alun_rede[0]['nome'], 'dickens silverio')
        self.assertEqual(alun_rede[1]['nome'], 'silvio_santos')

    def test_pes_alun_rede(self):
        self._pes_alun_by_rede()

    def _pes_alun_by_turma(self):
        self._create_aluno()
        alunos = self.facade.search_aluno_by_turma_facade('KND')
        self.assertEqual(alunos[0]['nome'], 'patric_estrela')
        self.assertEqual(alunos[1]['nome'], 'silvio_santos')

    def test_pesq_alun_t(self):
        self._pes_alun_by_turma()

    def _gravar_premiacao(self):
        from control.gestao_aprendizagem_controller import convertendo_str_in_dict
        # premios = {
        #     'medalhas': gamificacao_medalha(aluno, oa=oa),
        #     'moedas': gamificacao['moedas'],'''int'''
        #     'xp': gamificacao['xp'] '''int'''
        # }
        medalhas = ('1', '2', '3')
        premiacao = {
            'medalhas': medalhas,
            'moedas': 9,
            'xp': 10
        }
        self._create_estrutura()
        self.facade.gravar_premiacao(1, premiacao)
        aluno = self.facade.search_aluno_id_facade(1)
        self.assertEqual(aluno['pontos_de_vida'], '10')
        self.assertEqual(aluno['pontos_de_moedas'], '9')
        medalha = self.facade.get_medalhas_facade(1)
        for i in range(0,len(medalha)-1):
            mel = convertendo_str_in_dict(medalha[i].decode('UTF-8'))
            self.assertEqual(mel['id_medalha'],str(i+1))

    def test_gravar_premiacao(self):
        self._create_aluno()
        self._gravar_premiacao()

    def _armazenar_ultimo_jogo(self):
        self._create_aluno()
        self.facade.armazenar_ultimo_jogo_jogado(1, 'AV1UA1OA1')

    def _mostrar_ultimo_jogo_jogado(self):
        oa = self.facade.mostrar_ultimo_oa_jogado('1')
        self.assertEqual(oa, 'AV1UA1OA1')

    def test_armazenar_ultimo_jogo(self):
        self._armazenar_ultimo_jogo()
        self._mostrar_ultimo_jogo_jogado()

    def _get_medalhas(self):
        from control.gestao_aprendizagem_controller import convertendo_str_in_dict
        self._create_aluno()
        self._gravar_premiacao()
        alun = self.facade.search_aluno_id_facade(1)
        medalhas = self.facade.get_medalhas_facade(alun['id'])
        meld=medalhas[0].decode('UTF-8')
        melda=convertendo_str_in_dict(meld)
        self.assertEqual(melda['id_medalha'], '1')

    def test_get_medalhas(self):
        self._get_medalhas()

    def _test_all_aluno(self):
        pass

    """FIM TESTE USUARIO/ALUNO"""

    """INICIO TESTE OBSERVADOR"""

    def _create_observador(self):
        self._create_estrutura()
        rede = self.facade.search_estrutura_facade(TIPO_ESTRUTURA['rede'], 'Rede Conecturma')
        observador1 = self.facade.create_observador_facade(nome='Egg', senha='span', telefone='(21)9999-9999',
                                                           cpf='123456789', email='egg@span.com.br',
                                                           vinculo_rede=str(rede['id']), escola='0',
                                                           tipo=TIPO_USUARIOS['administrador'])

        existe = self.facade.search_observador_id_facade(1)
        self.assertIsNotNone(existe)
        observador2 = self.facade.create_observador_facade(nome='Monty', senha='python',
                                                           telefone='(21)9999-9999',
                                                           cpf='123456789', email='Monty@python.com.br',
                                                           tipo=TIPO_USUARIOS['gestor'], vinculo_rede="Nenhuma",
                                                           escola="1",
                                                           )
        existe1 = self.facade.search_observador_id_facade(2)
        self.assertIsNotNone(existe1)

        observador3 = self.facade.create_observador_facade(nome="diretor", senha="123", telefone="21 2569 6969",
                                                           email="tent@cool.os", tipo=TIPO_USUARIOS['diretor'],
                                                           rede="nao", vinculo_escola='1')

        existe2 = self.facade.search_observador_id_facade(3)
        self.assertIsNotNone(existe2)

        observador4 = self.facade.create_observador_facade(nome='Caio Lacildes', senha='123deoliveira4',
                                                           telefone='22001593', tipo=TIPO_USUARIOS['professor'],
                                                           escola='Fundaçao zeraldo oliveira', cpf='2015647892',
                                                           vinculo_turma='1',
                                                           vinculo_rede='Rede de pesca', email='seil@teste.br')

        existe3 = self.facade.search_observador_id_facade(4)
        self.assertIsNotNone(existe3)
        observador5 = self.facade.create_observador_facade(nome='Lucicreide', senha='624de12aveira4',
                                                           telefone='2054393', tipo=TIPO_USUARIOS['professor'],
                                                           vinculo_escola='1', cpf='20155666892',
                                                           vinculo_rede='Rede de pesca', email='seil@teste.br')
        existe4 = self.facade.search_observador_id_facade(5)
        self.assertIsNotNone(existe4)

    def _update_observador(self):

        observador1 = self.facade.search_observador_facade('Caio Lacildes')
        self.facade.update_observador_facade(id=observador1['id'], nome='Knight',
                                             email='knight@ni.com', telefone="21 999443243", cpf="9993245611",
                                             vinculo_turma='1', vinculo_escola='2')
        observador3 = self.facade.search_observador_tipo_nome_facade('3', 'Knight')
        self.assertEqual(observador3['nome'], 'Knight')
        self.assertEqual(observador3['email'], 'knight@ni.com')
        self.assertEqual(observador3['telefone'], "21 999443243")
        self.assertEqual(observador3['cpf'], "9993245611")
        self.assertEqual(observador3['vinculo_turma'], "1")
        self.assertEqual(observador3['vinculo_escola'], "2")


    def test_create_update_delete_observador(self):
        self._create_observador()
        self._update_observador()
        self._delete_observador()

    def _read_observador(self):
        self._create_observador()
        observador1 = self.facade.search_observador_facade('Egg')
        observador2 = self.facade.search_observador_facade('Monty')
        observador3 = self.facade.search_observador_facade('diretor')
        observador4 = self.facade.search_observador_facade('Caio Lacildes')
        observador = self.facade.read_observador_facade()
        x = 0
        for i in range(0, len(observador)):
            if self.facade.read_observador_facade()[i]['nome'] == 'Egg':
                self.assertEqual(observador[i]['email'], observador1['email'])
                self.assertEqual(observador[i]['telefone'], observador1['telefone'])
            elif self.facade.read_observador_facade()[i]['nome'] == 'Monty':
                self.assertEqual(self.facade.read_observador_facade()[i]['email'], observador2['email'])
            elif observador[i]['nome'] == observador3['nome']:
                self.assertEqual(observador[i]['email'], observador3['email'])
            elif observador[i]['nome'] == observador4['nome']:
                self.assertEqual(observador[i]['email'], observador4['email'])
            x += 1
        self.assertEqual(x, len(observador))

    def test_read_observador(self):
        self._read_observador()

    def _redefinir_senha(self):
        self._create_observador()
        observador = self.facade.search_observador_facade('Egg')
        self.facade.redefinir_senha_facade(observador['id'], 'naoseimesmo')
        observador_pos = self.facade.search_observador_facade('Egg')
        self.assertEqual(observador['id'], observador_pos['id'])
        self.assertNotEqual(observador['senha'], observador_pos['senha'])
        self.assertEqual(observador_pos['senha'], 'naoseimesmo')

    def test_redefinir_senha(self):
        self._redefinir_senha()

    def _search_observador_id(self):
        self._create_observador()
        observador = self.facade.search_observador_id_facade(1)
        self.assertEqual(observador['nome'], 'Egg')
        self.assertNotEqual(observador['nome'], 'egg')
        observador2 = self.facade.search_observador_id_facade(2)
        self.assertEqual(observador2['nome'], 'Monty')
        self.assertNotEqual(observador2['nome'], 'monty')

    def test_search_observador_id(self):
        self._search_observador_id()

    def _search_observador_email(self):
        self._create_observador()
        self._update_observador()
        observador = self.facade.search_observador_id_facade(4)
        observador1 = self.facade.search_observador_email_facade(observador['email'])
        # print(observador['vinculo_turma'][0].decode('UTF-8'))
        self.assertEqual(observador['nome'], observador1['nome'])
        self.assertEqual(observador['email'], observador1['email'])
        self.assertEqual(observador['senha'], observador1['senha'])
        self.assertEqual(observador['telefone'], observador1['telefone'])

    def test_search_observador_email(self):
        self._search_observador_email()

    def _search_observador(self):
        self._create_observador()
        observador1 = self.facade.search_observador_facade('Egg')
        self.assertEqual(observador1['nome'], 'Egg')
        self.assertEqual(observador1['senha'], 'span')
        self.assertEqual(observador1['telefone'], '(21)9999-9999')
        self.assertEqual(observador1['cpf'], '123456789')
        self.assertEqual(observador1['email'], 'egg@span.com.br')
        self.assertEqual(observador1['tipo'], '0')
        observador2 = self.facade.search_observador_facade('Ni')
        self.assertIs(observador2, None)

    def test_search_obs(self):
        self._search_observador()

    def _search_observador_tipo(self):
        self._create_observador()
        observador_adm = self.facade.search_observador_tipo_facade(TIPO_USUARIOS['administrador'])
        self.assertEqual(observador_adm[0]['nome'], 'Egg')
        observador_gestor = self.facade.search_observador_tipo_facade(TIPO_USUARIOS['gestor'])
        self.assertEqual(observador_gestor[0]['nome'], 'Monty')
        observador_diretor = self.facade.search_observador_tipo_facade(TIPO_USUARIOS['diretor'])
        self.assertEqual(observador_diretor[0]['nome'], 'diretor')
        observador_professor = self.facade.search_observador_tipo_facade(TIPO_USUARIOS['professor'])
        self.assertEqual(observador_professor[0]['nome'], 'Caio Lacildes')

    def test_search_observador_tipo(self):
        self._search_observador_tipo()

    def _search_observador_tipo_nome(self):
        observador1 = self.facade.search_observador_tipo_nome_facade(TIPO_USUARIOS['administrador'], 'Egg')
        observador1_1 = self.facade.search_observador_facade('Egg')
        self.assertEqual(observador1, observador1_1)

    def test_search_observador_tipo_nome(self):
        self._search_observador_tipo_nome()

    def _search_obsevador_by_rede(self):
        self._create_observador()
        self._create_estrutura()
        observador1 = self.facade.search_observador_id_facade(1)
        observador_rede1 = self.facade.search_observador_by_rede_facade('1')
        self.assertEqual(observador_rede1[0]['nome'], observador1['nome'])

    def test_search_observador_by_rede(self):
        self._search_obsevador_by_rede()

    def _search_observador_escola(self):
        self._create_observador()

    def test_search_obs_escola(self):
        self._search_observador_escola()

    def _delete_observador(self):
        observador1 = self.facade.read_observador_facade()
        escolhidos = []
        for observados in observador1:
            escolhidos.append(observados['id'])
        self.facade.delete_observador_facade(escolhidos)

    def _search_observador_turma(self):
        self._create_observador()
        professor1 = self.facade.search_observador_turma(1)
        self.assertEqual(professor1[0]['nome'], 'Caio Lacildes')

    def test_search_observador_turma(self):
        self._search_observador_turma()

    def _search_diretor_vinculo_escola(self):
        self._create_observador()
        diretor = self.facade.search_diretor_vinculo_escola_facade('1')
        self.assertEqual('diretor', diretor['nome'])

    def test_search_diretor_vinculo_escola(self):
        self._search_diretor_vinculo_escola()

    def _observador_in_turma(self):
        '''
        O id do observador em turma recebe uma lista
        :return:
        '''
        self._create_observador()
        professor = self.facade.search_observador_id_facade(5)
        professor1 = self.facade.search_observador_id_facade(4)
        lista_id = (professor['id'], professor1['id'])
        self.facade.observador_in_turma_facade(lista_id, '1')
        professor_dentro = self.facade.search_observador_turma('1')
        self.assertEqual(professor_dentro[1]['nome'], professor['nome'])

    def test_observador_in_turma(self):
        self._observador_in_turma()

    def _login_date(self):
        '''testavel via front e em parceria com o webtest'''
        pass

    def _pesquisa_email_facade(self):
        self._create_observador()
        observador = self.facade.search_observador_id_facade(1)
        obs = self.facade.pesquisa_email_facade(observador['email'])
        self.assertEqual(obs[0]['nome'], observador['nome'])

    def test_search_pesquisa_email(self):
        self._pesquisa_email_facade()

    # def _test_anotacoes(self):
    #     self._anotacoes_est

    # def _anotacoes_estrutura(self):
    #     self._create_escola()
    #     self._pesquisa_escola()
    #     mensagem2 = "Gosto dessa escola"
    #     mensagem = "Nossa escola deve melhorar"
    #     observador1 = self.facade.search_observador_inativos_facade("egg")
    #     gestor = self.facade.search_observador_inativos_facade("")
    #     self.facade.anotacoes_estrutura_baixo_facade(observador1.id, mensagem)
    #     self.facade.anotacoes_estrutura_cima_facade(gestor.id, mensagem2)
    #     self.assertEqual(observador1.anotacoes_estrutura_baixo[0], mensagem.encode('utf-8'))
    #     # self.assertEqual(gestor.anotacoes_estrutura_cima[0],mensagem2.encode('utf-8'))
    # rutura()

    """FIM TESTE OBSERVADOR"""

    """TESTE ESTRUTURAS"""

    def _create_estrutura(self):
        rede = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['rede'],
                                                   nome="Rede Conecturma",
                                                   telefone="(21)9999-9999")
        self.assertIsNot(rede, None)
        escola = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola'], nome='escola conecturma')
        self.assertIsNot(escola, None)
        escola_rede = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola'],
                                                          nome='escola da rede', vinculo_rede='1')
        self.assertIsNot(escola_rede, None)
        turma = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['turma'], nome='turma conecturma',
                                                    vinculo_escola='2', vinculo_rede='1')
        self.assertIsNot(turma, None)
        item_cabeca = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome='cabeca',
                                                          tipo_item=TIPO_ITEM['rosto'], descricao='uma cabeca',
                                                          descricao_completa='é so isso mesmo , uma cabeça , oq esperava?')
        self.assertIsNot(item_cabeca, None)
        item_ombro = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome='ombro',
                                                         tipo_item=TIPO_ITEM['corpo'], descricao='uma parte do corpo',
                                                         descricao_completa='é so isso mesmo , um ombro , oq esperava?')
        self.assertIsNot(item_ombro, None)
        item_joelho = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome='Joelho',
                                                          tipo_item=TIPO_ITEM['cor'],
                                                          descricao='uma parte do cu...elhiunho',
                                                          descricao_completa='é so isso mesmo , um cor , oq esperava?')
        self.assertIsNot(item_joelho, None)
        item_e_pe = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['item'], nome='e pe',
                                                        tipo_item=TIPO_ITEM['acessorio'],
                                                        descricao='uma parte do corpo, pe do exodia',
                                                        descricao_completa='é so isso mesmo , um pe , oq esperava?')
        self.assertIsNot(item_e_pe, None)
        medalha_socio = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['medalha'],
                                                            tipo_medalha=TIPO_MEDALHA_NOME['SocioEmocional'],
                                                            nome='social comunismo')
        self.assertIsNot(medalha_socio, None)
        medalha_jogo = self.facade.create_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['medalha'],
                                                           tipo_medalha=TIPO_MEDALHA_NOME['SocioEmocional'],
                                                           nome='fazendo joguinhos')
        self.assertIsNot(medalha_jogo, None)

        iten1 = self.facade.create_estrutura_facade(nome="burroquandofoge", tipo_estrutura=TIPO_ESTRUTURA['item'],
                                                    tipo_item='1', preco='0')
        self.assertIsNot(iten1, None)
        escola = self.facade.create_estrutura_facade(nome='Do bairro', bairro='de baixo', telefone='2266 6622',
                                                     numero='21 ', UF='RJ', cidade='Pindamonhagaba',
                                                     cep='22287111')

        self.assertIsNot(escola, None)
        turma1 = self.facade.create_estrutura_facade(nome="Knight", tipo_estrutura="3", serie="1", vinculo_escola="1",
                                                     quem_criou="Ni")
        self.assertIsNot(turma1, None)

        oa1 = facade.create_estrutura_facade(tipo_estrutura="7", nome="Estante", sigla_oa="UV1AV1UD1OA01",
                                             aventura="AV1",
                                             descricao="Distinguir coisas onde podemos encontrar números (Números e Operações - algebra e Funções)",
                                             tipo_oa=TIPO_OAS_ID["MINI_GAME"], unidade="1", sigla_descritor="NU1.01",
                                             nome_descritor="Estante de Leitura",
                                             descricao_descritor="Localizar acontecimentos no tempo (ontem, hoje, amanhã)",
                                             serie="1", disciplina="2")
        self.assertIsNotNone(oa1)
        oa2 = facade.create_estrutura_facade(tipo_estrutura="7", nome="Acerte as Letras", sigla_oa="UV1AV1UD1OA02",
                                             aventura="AV1",
                                             descricao="Diferenciar letras de outros sinais gráficos, como os números e os sinais de pontuação (SEA - Sistema de Escrita Alfabética)",
                                             tipo_oa=TIPO_OAS_ID["MINI_GAME"], unidade="1", sigla_descritor="SE1.02",
                                             nome_descritor="Acerte as Letras",
                                             descricao_descritor="Compreender a função das letras e do alfabeto",
                                             serie="1",
                                             disciplina="1")
        self.assertIsNotNone(oa2)

    def test_create_estrutura(self):
        self._create_estrutura()

    def _read_estrutura(self):
        self._create_estrutura()
        read = facade.read_estrutura_facade(TIPO_ESTRUTURA['escola'])
        self.assertEqual(read[0]['nome'], 'escola conecturma')

    def test_read_estrutura(self):
        self._read_estrutura()

    def _update_rede(self):
        self._create_estrutura()
        rede1 = self.facade.search_estrutura_facade(tipo_estrutura="1", nome="Rede Conecturma")
        self.assertEqual(rede1['nome'], 'Rede Conecturma')
        estrutura = {'id': '1', 'telefone': '(11)8888-8888', 'nome': 'Ni'}
        rede_up = self.facade.update_estrutura_facade(estrutura=estrutura)
        rede = self.facade.search_estrutura_facade(tipo_estrutura="1", nome="Ni")
        self.assertEqual(rede['nome'], "Ni")
        self.assertEqual(rede['telefone'], "(11)8888-8888")

    def _update_escola(self):
        self._create_estrutura()
        escola = self.facade.search_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola'], nome="Do bairro")
        self.assertEqual(escola['nome'], 'Do bairro')
        estrutura = {'telefone': '33355567', 'nome': 'Ni', 'vinculo_rede': 'abelhinha',
                     'cep': '22270 999', 'endereco': 'rua do teste', 'numero': '666', 'cidade': 'RIO DE JANEIRO',
                     'estado': 'RJ', 'id': str(escola['id'])}

        self.facade.update_estrutura_facade(estrutura=estrutura)
        escola2 = self.facade.search_estrutura_facade(tipo_estrutura=TIPO_ESTRUTURA['escola'], nome='Ni')

        self.assertEqual(escola2['nome'], 'Ni')
        self.assertEqual(escola2['endereco'], 'rua do teste')
        self.assertEqual(escola2['numero'], '666')
        self.assertEqual(escola2['vinculo_rede'], 'abelhinha')
        self.assertEqual(escola2['telefone'], '33355567')
        self.assertEqual(escola2['endereco'], 'rua do teste')

    def test_update_estrutura(self):
        self._update_rede()

    def test_update_escola(self):
        self._update_escola()

    def _pesquisa_estrutura(self):
        self._create_estrutura()
        rede = self.facade.search_estrutura_facade(tipo_estrutura="1", nome="Rede Conecturma")
        self.assertEqual(rede['nome'], 'Rede Conecturma')
        rede1 = self.facade.search_estrutura_facade(tipo_estrutura="2", nome="escola conecturma")
        self.assertEqual(rede1['nome'], 'escola conecturma')
        rede = self.facade.search_estrutura_facade(tipo_estrutura="1", nome="Rede Conecturma")
        self.assertEqual(rede['nome'], 'Rede Conecturma')
        rede1 = self.facade.search_estrutura_facade(tipo_estrutura="2", nome="escola conecturma")
        self.assertEqual(rede1['nome'], 'escola conecturma')

    def _pesquisa_escola(self):
        self._create_estrutura()
        escola = self.facade.search_estrutura_facade(tipo_estrutura="2", nome="Do bairro")
        self.assertEqual(escola['nome'], "Do bairro")
        escola1 = self.facade.search_estrutura_facade(tipo_estrutura="2", nome="Sily walk")
        self.assertEqual(escola1, [])

    def _pesquisa_estrutura_id(self):
        self._create_estrutura()
        estrutura = self.facade.search_estrutura_id_facade(1)
        self.assertEqual(estrutura['nome'], 'Rede Conecturma')

    def _search_estrutura_escola_by_rede(self):
        escola = self.facade.search_estrutura_escola_by_rede_facade('1')
        self.assertEqual(escola[0]['nome'], 'escola da rede')

    def _search_estrutura_turma_by_rede(self):
        turma = self.facade.search_estrutura_turma_by_rede_facade('1')
        self.assertEqual(turma[0]['nome'], 'turma conecturma')

    def _search_estrutura_turma_by_escola(self):
        turma = self.facade.search_estrutura_turma_by_escola_facade('2')
        self.assertEqual(turma[0]['nome'], 'turma conecturma')

    def _search_oa_by_type_and_aventura_facade(self):
        oa = self.facade.search_oa_by_type_and_aventura_facade(aventura='AV1', disciplina='2')
        self.assertEqual(oa[0]['nome'], 'Estante')

    def _search_descritor_serie_facade(self):
        desc = self.facade.search_descritor_serie_facade('1')
        self.assertEqual(desc[1]['nome'], 'Acerte as Letras')

    def test_pesquisas_estrutura(self):
        self._pesquisa_estrutura()
        self._pesquisa_escola()
        self._pesquisa_estrutura_id()
        self._search_estrutura_escola_by_rede()
        self._search_estrutura_turma_by_rede()
        self._search_oa_by_type_and_aventura_facade()
        self._search_descritor_serie_facade()


    """FIM TESTE TURMA """

    """TESTE FACADE HISTORICO"""

    def _create_historico(self):
        hist = self.facade.create_historico_facade(nome_usuario='administrador', acao='recriar um filho da mae',
                                                   momento=datetime.datetime(2016, 5, 2, 14, 25, 11))
        self.assertIsNot(hist, None)

    def _read_historico(self):
        historico = self.facade.read_historico_facade()
        self.assertEqual(list(historico)[0]['nome_usuario'], 'administrador')

    def test_create_read_historico(self):
        self._create_historico()
        self._read_historico()

    def _hist_dados_cadastrado(self):
        self._create_historico()
        dados = {'nome': 'xinchorino', 'facilidade': 20, 'cao': 'nao', 'gato': 'noop'}
        self.facade.historico_de_dados_cadastrados_facade(1, dados)
        teste = self.facade.ver_dados_cadastrados_facade(1)
        self.assertEqual(teste['nome'], 'xinchorino')
        self.assertEqual(teste['facilidade'], '20')
        self.assertEqual(teste['cao'], 'nao')
        self.assertEqual(teste['gato'], 'noop')

    def test_hist_dados_cadastro(self):
        self._hist_dados_cadastrado()

    def _search_historico_id_facade(self):
        self._create_historico()
        hist = self.facade.search_historico_id_facade(1)
        self.assertEqual(hist['nome_usuario'], 'administrador')
        self.assertEqual(hist['acao'], 'recriar um filho da mae')

    def _search_historico_nome(self):
        self._create_historico()
        hist = self.facade.search_historico_nome_facade('administrador')
        self.assertEqual(hist[0]['nome_usuario'], 'administrador')
        self.assertEqual(hist[0]['acao'], 'recriar um filho da mae')

    def _search_hist_acao(self):
        self._create_historico()
        hist = self.facade.search_historico_acao_facade('recriar um filho da mae')
        self.assertEqual(hist[0]['nome_usuario'], 'administrador')

    def test_search_historico(self):
        self._search_historico_id_facade()
        self._search_historico_nome()
        self._search_hist_acao()

    """FIM TESTE FACADE HISTORICO"""

    """ TESTE DE JOGO FACADE"""

    # {id'_aluno': '2', 'unidade': 'UV1AV1UD1', 'objeto_aprendizagem': 'UV1AV1UD1OA02'}
    def _create_oa_concluido_facade(self):
        oa_criad = self.facade.create_oa_concluido_facade(id_aluno='1', unidade='UV1AV1UD1',
                                                          objeto_aprendizagem='UV1AV1UD1OA02')
        self.assertIsNotNone(oa_criad)

    def test_create_oa_conluido(self):
        self._create_oa_concluido_facade()

    def _search_desempenho_concluido_id_aluno_facade(self):
        self._create_oa_concluido_facade()
        teste = self.facade.unidade_teste_facade(2, 'UV1AV1UD1')
        self.assertEqual(teste[0]['objeto_aprendizagem'], 'UV1AV1UD1OA02')

    def test_search_desempenho_concluido(self):
        self._search_desempenho_concluido_id_aluno_facade()

    def _unidade_concluida_facade(self):
        self._create_oa_concluido_facade()
        teste = self.facade.unidade_concluida_facade(2, 'UV1AV1UD1')
        self.assertEqual(teste[0]['objeto_aprendizagem'], 'UV1AV1UD1OA02')

    def _search_oa_facade(self):
        self._create_oa_concluido_facade()

    """FIM DE TESTE DE JOGO"""

    """TESTE INATIVOS"""

    def _transferir_atores_inativos(self):
        self._anotacoes_no_aluno()
        self._create_observador()

        # iten1 = self.facade.create_estrutura_facade(nome="burroquandofoge", '1', preco=0)
        # self.assertIsNot(iten1, None)

        aluno1 = self.facade.create_aluno_facade(nome="thanos", escola="Estalo", senha="123", vinculo_rede="0",
                                                 matricula='2929')
        # item2 = self.facade.search_estrutura_facade("burroquandofoge")
        self.assertEqual(aluno1, True)
        # self.assertIsNot(item2,None)

        alunoer1 = self.facade.search_aluno_nome_objeto_facade("egg")
        self.assertIsNot(alunoer1, None)

        aluno2 = self.facade.search_aluno_nome_objeto_facade("thanos")
        self.assertIsNot(aluno2, None)

        aluno2_pos = self.facade.search_aluno_nome_objeto_facade("thanos")
        self.assertIsNot(aluno2_pos, None)

        observador1 = self.facade.search_observador_inativos_facade("Monty")
        self.assertIsNot(observador1, None)

        inativados = [alunoer1, aluno2_pos, observador1]
        self.facade.create_zInativos_atores_facade(inativados)

        ovo_morto = self.facade.pesquisa_inativos_facade("egg")
        self.assertIsNot(ovo_morto, None)

        mensagem = "Isto é uma mensagem de teste"
        mensagem2 = "tetativa..."
        ovo_falecido = self.facade.pesquisa_aluno_nome_objeto_facade("egg")
        self.assertEqual(ovo_falecido, [])
        self.assertEqual(ovo_morto.nome, alunoer1.nome)
        self.assertEqual(ovo_morto.anotacoes_aluno[0], mensagem.encode('utf-8'))
        self.assertEqual(ovo_morto.anotacoes_aluno[1], mensagem2.encode('utf-8'))

        thanos_morto = self.facade.pesquisa_inativos_facade("thanos")
        self.assertEqual(thanos_morto.nome, aluno2_pos.nome)
        self.assertEqual(thanos_morto.senha, aluno2_pos.senha)
        self.assertEqual(thanos_morto.tipo_usuario, aluno2_pos.tipo_aluno)
        self.assertEqual(thanos_morto.cor, aluno2.cor)
        self.assertEqual(thanos_morto.rosto, aluno2.rosto)
        self.assertEqual(thanos_morto.acessorio, aluno2.acessorio)
        self.assertEqual(thanos_morto.corpo, aluno2.corpo)
        self.assertEqual(thanos_morto.pontos_de_vida, aluno2.pontos_de_vida)
        self.assertEqual(thanos_morto.pontos_de_moedas, aluno2.pontos_de_moedas)
        self.assertEqual(thanos_morto.vinculo_escola, aluno2.vinculo_escola)
        self.assertEqual(thanos_morto.vinculo_turma, aluno2.vinculo_turma)
        self.assertEqual(aluno2.itens_comprados[-1], thanos_morto.itens_comprados[0])

        observador1_morto = self.facade.pesquisa_inativos_facade("Monty")
        self.assertIsNot(observador1_morto, None)
        observador1_inexistente = self.facade.search_observador_inativos_facade("Monty")
        self.assertEqual(observador1_inexistente, [])

    def _inativar_estruturas(self):
        self._create_escola()
        self.facade.search_escola_facade()
        self.facade.create_zInativos_estrutura_facade()

    def _ressuscitar_usuarios(self):
        self._transferir_atores_inativos()
        ovo_morto = self.facade.pesquisa_inativos_facade("egg")
        self.assertIsNot(ovo_morto, None)

        ovo_vivo = self.facade.reativar_usuario_facade(ovo_morto)
        self.assertEqual(ovo_vivo, True)

        fenix = self.facade.search_aluno_nome_facade("egg")
        self.assertIsNot(fenix, None)

        aluno1 = self.facade.search_aluno_nome_facade("egg")
        self.assertEqual(fenix.senha, aluno1.senha)

        cem_observador1 = self.facade.pesquisa_inativos_facade("Monty")
        self.assertIsNot(cem_observador1, None)

        observador1 = self.facade.search_observador_inativos_facade("Monty")
        self.assertIsNot(observador1, None)

        observador = self.facade.reativar_usuario_facade(cem_observador1)
        self.assertEqual(observador, True)

        cem_observador_pos = self.facade.pesquisa_inativos_facade("Monty")
        self.assertEqual(cem_observador_pos, [])

    def _read_inativados(self):
        self._transferir_atores_inativos()
        read_cem = self.facade.read_inativos_facade()
        self.assertIsNot(read_cem, None)

    def _test_create_atores_inativos(self):
        self._transferir_atores_inativos()

    def _test_create_estruturas_inativas(self):
        self._inativar_estruturas()

    def _test_reativar_usuario(self):
        self._ressuscitar_usuarios()

    def _test_read_inativos(self):
        self._read_inativados()

    def tearDown(self):
        self.facade.apagartudo()

    # def test_substituto_de_webtest(self):
    #     self._create_observador()

    # def _comprar_item(self):
    #     self._create_estrutura()
    #     self._create_aluno()
    #     aluno1 = self.facade.search_aluno_nome_objeto_facade("egg")
    #     item1 = self.facade.search_estrutura_facade(nome="burroquandofoge", tipo_estrutura="4")
    #     self.facade.compra_item_facade(aluno1.id, item1['id'])
    #     aluno=self.facade.ver_item_comprado_facade(aluno1.id)
    #     print('alun',aluno)
    #     self.assertIn(str(item1['id']), aluno1.itens_comprados[-1].decode('utf-8'))

    #
    # def test_compra_item(self):
    #     self._comprar_item()
    #
    # def _ver_iten_comprado(self):
    #     self._comprar_item()
    #     aluno1 = self.facade.search_aluno_nome_objeto_facade("egg")
    #     iten = self.facade.ver_item_comprado_facade(aluno1.id)
    #     self.assertEqual([(aluno1.itens_comprados[0].decode('utf-8'))], iten)
    #
    # def test_ver_itens_comprados(self):
    #     self._ver_iten_comprado()
    #
    # def _equipar_item_facade(self):
    #     self._comprar_item()
    #     aluno1 = self.facade.search_aluno_nome_facade("egg")
    #     iten = self.facade.search_estrutura_facade(tipo_estrutura='5', nome="burroquandofoge")
    #     self.facade.equipar_item_facade(aluno1['id'], iten)
    #     aluno2 = self.facade.search_aluno_nome_facade("egg")
    #     self.assertEqual(aluno2['cor'], str(iten['id']))
    #
    # def test_equipar_item(self):
    #     self._equipar_item_facade()
    #
    # def _mostrar_avatar(self):
    #     self._equipar_item_facade()
    #     aluno1 = self.facade.search_aluno_nome_facade("egg")
    #     self.facade.avatar_facade(aluno1['id'])
    #     iten1 = self.facade.search_estrutura_facade(TIPO_ESTRUTURA['item'], "burroquandofoge")
    #     self.assertEqual(self.facade.avatar_facade(aluno1['id'])['cor'], str(iten1['id']))
    #     # self._delete_item()
    #
    # def test_ver_avatar(self):
    #     self._mostrar_avatar()

    # def _ja_possui_item(self):
    #     self._comprar_item()
    #     item = facade.ja_tem_item_facade('2')
    #     self.assertEqual(item[0], '5')
    #
    # def test_ja_possui_item(self):
    #     self._ja_possui_item()


if __name__ == '__main__':
    unittest.main()
