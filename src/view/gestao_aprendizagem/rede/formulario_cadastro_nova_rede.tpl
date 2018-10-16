<!--div da nova escola-->

    <div class="row row-impar">
        <div class="col-md-11 item-tabela-h" style="color:black">
            nova rede
        </div>
        <div class="col-md-1 item-tabela">
            <button id="dads" class="normalizar-botao" onclick="test(this.id);">
                <i class='fas fa-angle-up'></i>
            </button>
        </div>
    </div>

    <div class="row row-impar" id="nova-escola" style="display: block">
        <div class="container">
            <div id="teste" class="row new-scola">
                <!--conteudo interno do botao a partir daqui-->
                <div class="col-md-12">
                    <ul class="nav nav-tabs abas" role="tablist">
                        <li class="nav-item ">
                            <a class="nav-link active " data-toggle="tab" href="#dados-da-escola" role="tab" aria-controls="dados-da-escola" aria-selected="true">Dados da Gerais</a>
                        </li>
                    </ul>
                </div>

                <!-- aqui começa o conteudo das guias(navlink)  -->
                <div class="tab-content row-impar" id="nav-tabContent">
                    <div class="row">
                        <div class="tab-pane fade show active container active" role="tabpanel" aria-labelledby="home-tab" id="dados-da-escola">
                            <div class="row distanciamneto" style="margin-top: 30px">
                                <div class="offset-md-1 col-md-">
                                    <img src="/static/img/editar-foto.png">
                                </div>
                                <div class="col-md-8">
                                    <div class="row distanciamneto">
                                        <div class=" col-md-6">
                                            <label for="nome" style="background-color: inherit;">Nome:
                                                <span style="color:#ff0000">*</span>
                                            </label>
                                            <input type="text" class="form-control" size="30" name="" id="nome" onchange="document.getElementById('nome').style.boxShadow = 'none'" value="">
                                        </div>
                                        <div class="col-md-6" style="padding-left: 10px">
                                            <label for="CNPJ">CNPJ</label>
                                            <br>
                                            <input type="text" size="25" class="form-control" name="" id="cnpj">
                                        </div>
                                    </div>
                                    <div class="row distanciamento">
                                        <div class="col-md-6">
                                            <label for="telefone">Telefone:
                                                <span style="color:#ff0000">*</span>
                                            </label>
                                            <input type="text" class="form-control" size="26" name="" id="telefone" onchange="document.getElementById('telefone').style.boxShadow = 'none'" value="">
                                        </div>
                                          <div class="col-md-6">
                                            <label for="data_de_criacao">Data de Criação:
                                            </label>
                                            <input type="text" class="form-control" size="26" name="" id="data_de_criacao"  value="" disabled>
                                        </div>

                                    </div>
                                    <!--fim da div dos dados ao lado da imagem-->
                                </div>
                                <div class="offset-md-1 row distanciamento">
                                    <div class="col-md-6">
                                        <label for="endereco">Endereço</label>
                                        <input type="text" class="form-control" size="50" name="endereco" id="endereco">
                                    </div>
                                    <div class="col-md-1" style="padding-left: 10px ;">
                                        <label for="numero">Numero</label>
                                        <input type="text" class="form-control" size="5" name="numero" id="numero">
                                    </div>
                                    <div class="col-md-4" style="padding-left: 9px ;">
                                        <label for="bairro">Bairro</label>
                                        <input type="text" class="form-control" size="24" name="bairro" id="bairro">
                                    </div>
                                </div>
                                <div class="offset-md-1 row distanciamento">
                                    <div class="col-md-6">
                                        <label for="complemento">Complemento</label>
                                        <input type="text" class="form-control" size="50" name="endereço" id="complemento">
                                    </div>
                                    <div class="col-md-5" style="padding-left: 10px ;">
                                        <label for="cep">CEP</label>
                                        <input type="text" class="form-control" size="32" name="cep" id="cep">
                                    </div>
                                </div>
                                <div class="offset-md-1 row distanciamento">
                                    <div class="col-md-6">
                                        <label for="estado">Estado</label>
                                        <input type="text" class="form-control" size="50" name="estado" id="estado">
                                    </div>
                                    <div class="col-md-5" style="padding-left: 10px ;">
                                        <label for="municipio">Municipio</label>
                                        <input type="text" class="form-control" size="32" name="municipio" id="municipio">
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- aqui termina o conteudo da guia do dados de escola  -->
                        <br>
                    </div>
                    <div class="container" style="margin-top:20px;margin-bottom: 20px">
                        <div class="row">
                            <div class="offset-md-9 distanciamento">
                                <button type="submit" class="botao-salvar" onclick="cadastro_rede()" style="margin-left: 10px;">salvar</button>
                                <button class="botao-salvar" style="background-color:#ff0000" onclick='document.getElementById("new_school").style.display = "none"'>cancelar</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!--fim do nova escola-->
            <!-- acordeon -->
        </div>
    </div>

<script>
    var date = new Date;
    document.getElementById('data_de_criacao').value = date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear();
</script>