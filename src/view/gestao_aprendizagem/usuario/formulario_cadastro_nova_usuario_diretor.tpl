<!--div da nova escola-->

<div class="row row-impar">
    <div class="col-md-11 item-tabela-h" style="color:black">
        Novo Diretor
    </div>
    <div class="col-md-1 item-tabela">
        <button id="diretor" class="normalizar-botao" onclick="test(this.id);">
            <i class='fas fa-angle-up'></i>
        </button>
    </div>
</div>
<div class="row row-impar" id="novo-diretor" style="display: block">
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
                                <input type="text" class="form-control" size="30" name="" id="diretor_nome" onchange="document.getElementById('diretor_nome').style.boxShadow = 'none'">
                            </div>
                            <div class="col-md-4" style="padding-left: 10px">
                                <label for="data">Data de nascimeto</label>
                                <span style="color:#ff0000">*</span>
                                <br>
                                <input type="date" size="25" class="form-control" required name="" id="diretor_nascimento" onchange="document.getElementById('diretor_nascimento').style.boxShadow = 'none'">
                            </div>
                            <div class="col-md-4">
                                <label for="telefone">email</label>
                                <span style="color:#ff0000">*</span>
                                <input type="email" size="25" class="form-control" placeholder="exemplo@exemplo.com"  required name="" id="diretor_email" onchange="emailValidador('diretor_email')">
                            </div>
                            <div class="col-md-12">
                                <label for="telefone">Escola</label>
                                <select id="diretor_escola" class="custom-select custom-select-md">
                                    % for i in escolas:
                                        <option value="{{i['id']}}">{{i['nome']}}</option>
                                    % end
                                </select>
                            </div>
                        </div>
                    </div>
                    <!-- aqui termina o conteudo da guia do dados de escola  -->
                    <br>
                </div>
                <div class="container" style="margin-top:20px;margin-bottom: 20px">
                    <div class="row">
                        <div class="offset-md-9 distanciamento"><!--nao existe\/-->
                            <button type="submit" class="botao-salvar" onclick="cadastro_usuario('diretor')"
                                    style="margin-left: 10px;">salvar
                            </button>
                            <button class="botao-salvar" style="background-color:#ff0000"
                                    onclick='document.getElementById("2").style.display = "none"'>cancelar
                            </button>
                            <div class="col-md-1">
                            <img id= "loading" src="/static/img/loading.gif" style="margin-left:10px;margin-top:20px;display:none;">
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!--fim do nova escola-->
        <!-- acordeon -->
    </div>
</div>
