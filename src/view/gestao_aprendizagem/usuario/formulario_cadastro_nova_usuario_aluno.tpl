<!--div da nova escola-->

<div class="row row-impar">
    <div class="col-md-11 item-tabela-h" style="color:black">
        Novo Aluno
    </div>
    <div class="col-md-1 item-tabela">
        <button id="aluno" class="normalizar-botao" onclick="test(this.id);">
            <i class='fas fa-angle-up'></i>
        </button>
    </div>
</div>
<div class="row row-impar" id="novo-aluno" style="display: block">
    <div class="container">
        <div id="teste" class="row new-scola">
            <!--conteudo interno do botao a partir daqui-->
            <div class="col-md-12">
                <ul class="nav nav-tabs abas" role="tablist">
                    <li class="nav-item ">
                        <a class="nav-link active " data-toggle="tab" href="#dados-da-escola" role="tab"
                           aria-controls="dados-da-escola" aria-selected="true">Dados da Gerais</a>
                    </li>
                </ul>
            </div>

            <!-- aqui começa o conteudo das guias(navlink)  -->
            <div class="tab-content row-impar" id="nav-tabContent">
                <div class="row">
                    <div class="tab-pane fade show active container active" role="tabpanel" aria-labelledby="home-tab"
                         id="dados-da-escola">
                        <div class="row distanciamneto" style="margin-top: 30px; margin-right: 0px;">
                            <div class=" col-md-4">

                                <label for="nome" style="background-color: inherit;">Nome Completo
                                    <span style="color:#ff0000">*</span>
                                </label>
                                <input type="text" class="form-control" size="30" name="" id="aluno_nome"
                                       onchange="document.getElementById('aluno_nome').style.boxShadow = 'none'">
                            </div>
                            <div class="col-md-4" style="padding-left: 10px">
                                <label for="data">Data de nascimeto</label>
                                <span style="color:#ff0000">*</span>
                                <br>
                                <input type="date" size="25" class="form-control"  name="" id="aluno_nascimento" onchange="document.getElementById('aluno_nascimento').style.boxShadow = 'none'">
                            </div>
                            <div class="col-md-4">
                                <label for="telefone">Sexo</label>
                                <select id="aluno_sexo" class="custom-select custom-select-md">
                                    <option value="1">Masculino</option>
                                    <option value="2">Feminino</option>
                                </select>
                            </div>
                            <div class="col-md-12">
                                <label for="telefone">Escola</label>
                                <span style="color:#ff0000">*</span>
                                <select id="aluno_escola" class="custom-select custom-select-md">
                                    % if isinstance(escolas, list):
                                        % for i in escolas:
                                            <option value="{{i['id']}}">{{i['nome']}}</option>
                                        % end
                                    % else:
                                        <option value="{{escolas['id']}}">{{escolas['nome']}}</option>
                                    % end
                                </select>
                            </div>
                            <div class="col-md-12" style="margin-top: 10px;">
                                <label for="telefone">Turma</label>
                                <select id="aluno_turma" class="custom-select custom-select-md">
                                    %if tipo != '3':
                                        <option value="0"></option>
                                        % for i in turmas:
                                            <option value="{{i['id']}}">{{i['nome']}}</option>
                                        % end
                                    %else:
                                        % for i in turmas:
                                            <option value="{{i['id']}}">{{i['nome']}}</option>
                                        % end
                                    %end
                                </select>
                            </div>
                        </div>
                    </div>
                    <!-- aqui termina o conteudo da guia do dados de escola  -->
                    <br>
                </div>
                <div class="container" style="margin-top:20px;margin-bottom: 20px">
                    <div class="row">
                        <div class="offset-md-8 distanciamento"><!--nao existe\/-->
                            <button type="submit" class="botao-salvar" onclick="cadastro_usuario('aluno')"
                                    style="margin-left: 10px;">salvar
                            </button>
                            <button class="botao-salvar" style="background-color:#ff0000"
                                    onclick='document.getElementById("4").style.display = "none"'>cancelar
                            </button>
                        </div>
                        <div class="col-md-1">
                            <img id= "loading" src="/static/img/loading.gif" style="margin-left:10px;margin-top:20px;display:none;">
                        </div>

                    </div>
                </div>
            </div>
        </div>
        <!--fim do nova escola-->
        <!-- acordeon -->
    </div>
</div>
