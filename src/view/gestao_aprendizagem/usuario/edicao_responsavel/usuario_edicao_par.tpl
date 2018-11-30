

<div class="col-md-12" id="id-nossa-escola" style="padding:0">
<div style="cursor: pointer;float:right;" class="col-md-3 item-tabela" id="" data-toggle="collapse" data-target="#collapse{{i['id']}}" aria-expanded="true" aria-controls="collapse{{i['id']}}" onclick="seta('a_setinha{{i['id']}}')">
    {{i['tipo']}}
</div>
<div style="cursor: pointer;" class="col-md-9 item-tabela" data-toggle="collapse" data-target="#collapse{{i['id']}}" aria-expanded="true" aria-controls="collapse{{i['id']}}" id="a_setinha{{i['id']}}" onclick="seta('a_setinha{{i['id']}}')">
    {{i['nome']}}
</div>
</div>
<!--fim das informaçoes da tabela-->

<!-- aqui começa os dados internos do acordeon -->
<div class="container">
    <div class="row">
        <div id="collapse{{i['id']}}" class="collapse col-md-12 item-tabela" role="tabpanel"
             aria-labelledby="headingOne" data-parent="#accordion">
            <div class="card-body">

                <div class="row">
                    <div class="col-md-12">
                        <ul class="nav nav-tabs abas" role="tablist">
                            <li class="nav-item ">
                                <a class="nav-link active " data-toggle="tab" href="#{{i['id']}}" role="tab"
                                   aria-controls="escola-do-rock" aria-selected="true">Dados da Gerais</a>
                            </li>
                            <!--<li class="nav-item">-->
                            <!--<button class="nav-link" data-toggle="tab" href="#{{i['id']}}-prof" aria-controls="escola-do-rock-prof" aria-selected="false">Professores</button>-->
                            <!--</li>-->
                        </ul>
                    </div>
                </div>
                <!-- aqui começa o conteudo das guias  -->
                <div class="tab-content">
                    <div class="tab-pane container active" id="{{i['id']}}">
                        <form>
                            <input type="hidden" id="observador_id{{i['id']}}" value="{{i['id']}}">
                            <div class="row distanciamento" style="margin-top: 30px">
                                <div class="col-md-12">
                                    <div class="row distanciamento" style="margin-left: 5px;">
                                        <div class=" col-md-">
                                            <label for="nome" style="background-color: inherit;">Nome:
                                                <span style="color:red">*</span>
                                            </label>
                                            <input type="text" placeholder="Escola do rock"
                                                   class="form-control disabledo{{i['id']}}" size="30" name=""
                                                   id="nome_obs{{i['id']}}" value="{{i['nome']}}" disabled>
                                        </div>
                                        <div class="col-md-" style="padding-left: 10px">
                                            <label style="background-color: inherit;">Aluno: </label>
                                            % for a in i['vinculo_aluno']:
                                                <input type="text" class="form-control disabledo{{a['id']}}" size="30" name="" id="nome_obs{{a['id']}}"
                                                       value="{{a['nome']}}" disabled>
                                            % end
                                        </div>
                                    </div>
                                    <h5>Acesso</h5>
                                    <div class="row distanciamento" style="margin-left: 5px;">

                                        <div class="col-md-">
                                            <label for="login">Email</label>
                                            <span style="color:#ff0000">*</span>
                                            <input type="text" size="25" class="form-control disabledo{{i['id']}}"
                                                   name="" id="email{{i['id']}}" value="{{i['email']}}" disabled>
                                        </div>
                                    </div>
                                    <!--fim da div dos dados ao lado da imagem-->
                                </div>
                            </div>
                        </form>
                    </div>
                    <!-- aqui termina o conteudo da guia do dados de escola  -->
                    <div class="row" style="margin-bottom: 10px">
                        % if tipo < '2':
                        <div class="col-md-1">
              <!--<span onclick="delete_estrutura({{i['id']}})" style="cursor:pointer;">
                <i class="far fa-trash-alt" style="color:#969696;"></i>
              </span>-->
                        </div>
                        % end
                         <div class="offset-md-10 col-md-1">
                       <div class="offset-md-8 col-md-2">
                        <button id="icone_edit{{i['id']}}"  class="botao-salvar" onclick="allow_edit({{i['id']}})" style="margin-left: 10px;">
                            Editar
                        </button>
                        <button onclick="update_observador({{i['id']}})" id="edit{{i['id']}}"  class="botao-salvar" style="margin-left: 10px;display:none;">
                            Salvar
                        </button>
                    </div>
                        </div>
                    </div>
                    <br>
                </div>


            </div>
        </div>
    </div>
</div>
</form>

<!--<div class="container">-->
<!--&lt;!&ndash;<div class="row" style="margin-bottom: 10px">-->

<!--<div class="col-md-1">-->
<!--<span onclick="delete_estrutura({{i['id']}})" style="cursor:pointer;">-->
<!--<i class="far fa-trash-alt" style="color:#969696;"></i>-->
<!--</span>-->
<!--</div>-->

<!--&gt;
                    <!--<div class="offset-md-10 col-md-1">-->
<!--<span onclick="update_escola({{i['id']}})" style="cursor:pointer;">-->
<!--<i class="fas fa-edit edit-ico" style="color: #969696;"></i>-->
<!--</span>-->
<!--</div>-->
<!--</div>&ndash;&gt;-->
<!--</div>-->




