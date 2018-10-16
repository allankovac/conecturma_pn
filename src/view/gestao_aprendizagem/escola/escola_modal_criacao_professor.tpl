<div class="modal fade" id="cadastroProf{{i['id']}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content row-impar" style="height: 349px;">
            <div class="modal-header">
                <div class="offset-md-1">
                    <h5 class="modal-title" id="exampleModalLabel">Novo Professor</h5>
                </div>
            </div>
            <div class="modal-body">
                <div class="row row-impar" id="novo-professor" style="display: block">
                    <div class="container">
                        <div id="teste" class="row new-scola">
                            <div class="tab-content row-impar" id="nav-tabContent">
                                <div class="row">
                                    <div class="tab-pane fade show active container active" role="tabpanel" aria-labelledby="home-tab"
                                         id="dados-da-escola">
                                        <div class="row">
                                            <input type="hidden" id="professor_escola_{{i['id']}}" value="{{i['id']}}">
                                            <div class="col-md-4 offset-md-1">
                                                <label for="nome" style="background-color: inherit;">Nome Completo
                                                    <span style="color:#ff0000">*</span>
                                                </label>
                                                <input type="text" class="form-control" size="30" name="" id="professor_nome_{{i['id']}}"
                                                       onchange="document.getElementById('professor_nome').style.boxShadow = 'none'">
                                            </div>
                                            <div class="col-md-6" style="padding-left: 10px">
                                                <label for="data">Data de nascimeto</label>
                                                <span style="color:#ff0000">*</span>
                                                <br>
                                                <input type="date" size="25" class="form-control" required name="" id="professor_nascimento_{{i['id']}}" onchange="document.getElementById('professor_nascimento').style.boxShadow = 'none'">
                                            </div>

                                            <div class="col-md-10 offset-md-1" style="margin-top: 10px;">
                                                <label for="telefone">Email</label>
                                                <span style="color:#ff0000">*</span>
                                                <input type="email" size="25" class="form-control" placeholder="exemplo@exemplo.com"  required name="" id="professor_email_{{i['id']}}" onchange="emailValidador('professor_email_{{i['id']}}')">
                                            </div>
                                            <div class="col-md-10 offset-md-1" style="margin-top: 10px;">
                                                <label for="turma">Turma</label>
                                                <select id="professor_turma_{{i['id']}}" class="custom-select custom-select-md">
                                                    <option value="0"></option>
                                                    %if i['turmas'] != []:
                                                        % for j in i['turmas']:
                                                            <option value="{{j['id']}}">{{j['nome']}}</option>
                                                        % end
                                                    % end
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                        <!-- aqui termina o conteudo da guia do dados de escola  -->
                                    <br>
                                </div>
                            </div>
                        </div>
                        <!--fim do nova escola-->
                        <!-- acordeon -->
                    </div>
                </div>
            </div> <!-- modal body-->
            <div class="modal-footer">
                <button type="submit" class="botao-salvar" onclick="cadastro_usuario_via_escola('professor', '{{i['id']}}')"   style="margin-left: 10px;">
                    salvar
                </button>
                <button class="botao-salvar" style="background-color:#ff0000"
                        onclick='document.getElementById("3").style.display = "none"'>cancelar
                </button>
            </div>
        </div>
    </div>
</div>