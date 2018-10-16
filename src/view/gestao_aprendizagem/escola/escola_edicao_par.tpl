<div style="cursor: pointer;" class="col-md-12 item-tabela " data-toggle="collapse" data-target="#collapse{{i['id']}}" aria-expanded="true"
       aria-controls="collapse{{i['id']}}" id="id-nossa-escola" onclick="seta('id-nossa-escola')">
    {{i['nome']}}
</div>
<!--fim das informaçoes da tabela-->
<!-- aqui começa os dados internos do acordeon -->
<div class="container">
    <div class="row">
    <div id="collapse{{i['id']}}" class="collapse col-md-12 item-tabela" role="tabpanel" aria-labelledby="headingOne" data-parent="#accordion">
        <div class="card-body">

            <div class="row">
                <div class="col-md-12">
                    <ul class="nav nav-tabs abas" role="tablist">
                        <li class="nav-item ">
                            <a class="nav-link active " data-toggle="tab" href="#{{i['id']}}" role="tab" aria-controls="escola-do-rock" aria-selected="true">Dados da Gerais</a>
                        </li>
                        <li class="nav-item">
                            <button class="nav-link" data-toggle="tab" href="#{{i['id']}}-coordenador" aria-controls="escola-do-rock-coordenador" aria-selected="false">Coordenadores</button>
                        </li>
                        <li class="nav-item">
                            <button class="nav-link" data-toggle="tab" href="#{{i['id']}}-prof" aria-controls="escola-do-rock-prof" aria-selected="false">Professores</button>
                        </li>
                        <li class="nav-item">
                            <button class="nav-link" data-toggle="tab" href="#{{i['id']}}-alunos" aria-controls="escola-do-rock-aluno" aria-selected="false">Alunos</button>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- aqui começa o conteudo das guias  -->
            <div class="tab-content ">
                <div class="tab-pane container active" id="{{i['id']}}">
                    <form>
                        <input type="hidden" id ="id_escola{{i['id']}}" value="{{i['id']}}">
                        <div class="row distanciamento" style="margin-top: 30px">
                            <div class="col-md-3">
                                <img src="/static/img/editar-foto.png" style="border:2px black;z-index: 0;">
                            </div>
                            <div class="col-md-9">
                                <div class="row distanciamento">
                                    <div class=" col-md-">
                                        <label for="nome" style="background-color: inherit;">Nome:
                                            <span style="color:red">*
                                                </span>
                                        </label>
                                        <input type="text" placeholder="Escola do rock" class="form-control disabled{{i['id']}}" size="30" name="" id="nome{{i['id']}}" value="{{i['nome']}}" disabled>
                                    </div>
                                    <div class="col-md-" style="padding-left: 10px">
                                        <label for="CNPJ">CNPJ</label>
                                        <br>
                                        <input type="text" size="24" class="form-control disabled{{i['id']}}" name="" id="cnpj{{i['id']}}" value="{{i['cnpj']}}" disabled>
                                    </div>
                                </div>
                                <div class="row distanciamento">
                                    <div class="col-md-">
                                        <label for="telefone">telefone:
                                            <span style="color:#ff0000">*</span>
                                        </label>
                                        <input type="text" class="form-control disabled{{i['id']}}" size="21" name="" id="telefone{{i['id']}}" value="{{i['telefone']}}" disabled>
                                    </div>
                                    <div class="col-md-" style="padding-left: 10px ;">
                                        <label for="diretor">Diretor</label>
                                        <br>
                                        <input type="text" size="33" class="form-control disabled{{i['id']}}" name="" id="diretor{{i['id']}}" value="{{i['vinculo_diretor_escola']}}" disabled>
                                    </div>
                                </div>
                                <div class="row distanciamento">
                                    <div class="col-md-">
                                        <label for="rede">Rede de Ensino:

                                        </label>
                                        % if i['vinculo_rede'] != '0':
                                            <input type="hidden" size="59" class="form-control " name="" id="rede{{i['id']}}" value="{{i['vinculo_rede_id']}}">
                                            <input type="text" size="59" class="form-control disabled{{i['id']}}" name="" value="{{i['vinculo_rede']}}" disabled>
                                        % else:
                                            <input type="text" size="59" class="form-control disabled{{i['id']}}" name="" value=" " disabled>
                                        %end
                                    </div>
                                </div>
                                <!--fim da div dos dados ao lado da imagem-->
                            </div>
                            <div class="offset-md-1 distanciamento row" style="">
                                <div class="col-md-6">
                                    <label for="endereco">Endereço</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="49" name="endereco" id="endereco{{i['id']}}" value="{{i['endereco']}}" disabled>
                                </div>
                                <div class="col-md-2" style="padding-left: 10px ;">
                                    <label for="numero">Numero</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="5" name="numero" id="numero{{i['id']}}" value="{{i['numero']}}" disabled>
                                </div>
                                <div class="col-md-4" style="padding-left: 10px;padding-right: 45px;">
                                    <label for="bairro">Bairro</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="24" name="bairro" id="bairro{{i['id']}}" value="{{i['bairro']}}" style="padding-right: 35px;" disabled>
                                </div>
                            </div>
                            <div class="offset-md-1  row">
                                <div class="col-md-6">
                                    <label for="complemento">Complemento</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="50" name="endereço" id="complemento{{i['id']}}" value="{{i['complemento']}}" disabled>
                                </div>
                                <div class="col-md-6" style="padding-left: 10px;padding-right: 45px;">
                                    <label for="cep">CEP</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="32" name="cep" id="cep{{i['id']}}" value="{{i['cep']}}" style="padding-right: 35px" disabled>
                                </div>

                            </div>
                            <div class="offset-md-1 row distanciamento">
                                <div class="col-md-6">
                                    <label for="estado">Estado</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="50" name="estado" id="estado{{i['id']}}" value="{{i['estado']}}" disabled>
                                </div>
                                <div class="col-md-6" style="padding-left: 10px;padding-right: 45px;">
                                    <label for="municipio">Municipio</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="32" name="municipio" id="municipio{{i['id']}}" value="{{i['municipio']}}" style="" disabled>
                                </div>
                            </div>
                        </div>
                </div>

                <div class="tab-pane fade aba-prof" id="{{i['id']}}-coordenador" role="tabpanel" aria-labelledby="{{i['nome']}}-coordenador">
                    %include('gestao_aprendizagem/escola/escola_edicao_aba_coordenador.tpl')
                </div>

                <div class="tab-pane fade aba-prof" id="{{i['id']}}-prof" role="tabpanel" aria-labelledby="{{i['nome']}}-prof">
                    %include('gestao_aprendizagem/escola/escola_edicao_aba_professor.tpl')
                </div>

                <div class="tab-pane fade aba-prof" id="{{i['id']}}-alunos" role="tabpanel" aria-labelledby="{{i['nome']}}-alunos">
                    %include('gestao_aprendizagem/escola/escola_edicao_aba_aluno.tpl')
                </div>

            </div>
            <div class="container">
                <div class="row" style="margin-bottom: 10px">
                    % if tipo != '2':
                        <div class="col-md-1">
                            <span onclick="delete_estrutura({{i['id']}})" style="cursor:pointer;">
                                <i class="far fa-trash-alt" style="color:#969696;"></i>
                            </span>
                        </div>
                    % end
                    <div class="offset-md-10 col-md-1">
                        <span onclick="allow_edit({{i['id']}})" class="{{i['id']}}" id="icone_edit{{i['id']}}"
                              style="cursor:pointer;">
                            <i class="fas fa-edit edit-ico" style="color: #969696;padding-right: 12px;"></i>
                        </span>
                        <span onclick="update_escola({{i['id']}})" id="edit{{i['id']}}"
                              style="cursor:pointer;display:none;">
                            <i class="far fa-save fa-lg" style="color: #969696;padding-left: 7px;"></i>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </form>
        <!-- Modal -->
        %include('gestao_aprendizagem/escola/escola_modal_criacao_professor.tpl')
        %include('gestao_aprendizagem/escola/escola_modal_criacao_coordenador.tpl')
        %include('gestao_aprendizagem/escola/escola_modal_criacao_aluno.tpl')
    </div>
</div>
