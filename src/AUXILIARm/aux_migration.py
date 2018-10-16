from bottle import *
from walrus import *
from facade.facade_main import *
from control.dicionarios import *
from passlib.hash import sha512_crypt

facade=Facade()

facade.create_estrutura_facade(nome='escola E',tipo_estrutura=TIPO_ESTRUTURA['escola'],telefone='21 55555555', cnpj='054782548')
facade.create_estrutura_facade(nome='rede R',tipo_estrutura=TIPO_ESTRUTURA['rede'],telefone='21 22556848', cnpj='20115482',vinculo_escola='1')
facade.create_observador_facade(nome='aaJoao d', telefone='21979645254', tipo=TIPO_USUARIOS['diretor'], vinculo_escola='1', email='lalala@gmail.com', senha='@onde2929', cpf='04432547' )
facade.create_observador_facade(nome='Paulo g', tipo=TIPO_USUARIOS['gestor'], telefone='2125243578', vinculo_escola='1', email='saijsa@huahsa.com',vinculo_rede='2')
facade.create_observador_facade(nome='AAAAAAA g', tipo=TIPO_USUARIOS['gestor'], telefone='25696969', vinculo_escola='1', email='organizaçao@huahsa.org',vinculo_rede='2')
facade.create_observador_facade(nome='Sorte G', tipo=TIPO_USUARIOS['gestor'], telefone='0800 MIL', vinculo_escola='1', email='SAUDADRES@huahsa.com',vinculo_rede='2')
facade.create_observador_facade(nome='AZAR d', telefone='0800 2015 05', tipo=TIPO_USUARIOS['diretor'], vinculo_escola='1', email='PACIENCIA@gmail.com', cpf='04432547' )
facade.create_observador_facade(nome='PEDANTE d', telefone='0800 0500 2099', tipo=TIPO_USUARIOS['diretor'], vinculo_escola='1', email='DONACHICA@gmail.com', cpf='04432547' )

for x in range(0,4):
    facade.create_estrutura_facade(nome="nome" + str(x), vinculo_escola='1',tipo_estrutura=TIPO_ESTRUTURA['turma'],serie='2')
    facade.create_observador_facade(nome='aagestor'+str(x),senha='@onde2929', telefone='21979645254', tipo=TIPO_USUARIOS['gestor'],
                                    vinculo_escola='1', email='tent@cool.'+str(x)+'s', cpf='04432547')

for x in range(0,10):
    if x%3==0:

        facade.create_observador_facade(nome='aprofessor'+ str(x)
                                        ,senha='123'+str(x),
                                        telefone='telefone',
                                        email='email@email.seila'+str(x),
                                        tipo=TIPO_USUARIOS['professor'],
                                        vinculo_escola='1',vinculo_turma='2')
    elif x%5 ==0:

        facade.create_observador_facade(nome='professor' +str(x), senha='123' +str(x), telefone='telefone',
                                        email='email@email' +str(x) + 'seila', tipo=TIPO_USUARIOS['professor'],
                                        vinculo_escola='1', vinculo_turma='3')
    elif x%7:
        facade.create_observador_facade(nome='professor' + str(x), senha='123' + str(x), telefone='telefone',
                                        email='email@email' + str(x) + 'seila', tipo=TIPO_USUARIOS['professor'],
                                        vinculo_escola='1', vinculo_turma='4')
    else:
        facade.create_observador_facade(nome='professor' + str(x), senha='123' + str(x), telefone='telefone',
                                        email='email@email' + str(x) + 'seila', tipo=TIPO_USUARIOS['professor'],
                                        vinculo_escola='1', vinculo_turma='5')
# for x in range(0, 20):
#     if x % 3 == 0 and x!=15 :
#
#         facade.create_aluno_facade(nome='aluno'+str(x) ,matricula="234522"+str(x) ,nome_login="aluno"+str(x) , senha="abcd",email="tent@cul.com"+str(x),vinculo_escola="1",vinculo_turma='2')
#     elif x % 5 == 0:
#
#         facade.create_aluno_facade(nome='aluno' + str(x), matricula="234522" + str(x), nome_login="aluno" + str(x),
#                                    senha="abcd", email="tent@cul.com" + str(x), vinculo_escola="1",
#                                    vinculo_turma='3')
#     elif x%15==0:
#
#         facade.create_aluno_facade(nome='aluno' + x, matricula="234522" + x, nome_login="aluno" + x, senha="abcd",
#                                    email="tent@cul.com" + x, vinculo_escola="1", vinculo_turma='4')
#     else:
#
#         facade.create_aluno_facade(nome='aluno' + str(x), matricula="234522" + str(x), nome_login="aluno" + str(x),
#                                    senha="abcd", email="tent@cul.com" + str(x), vinculo_escola="1",
#                                    vinculo_turma='5')
