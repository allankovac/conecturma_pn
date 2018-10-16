<!--informaçoes-->
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
                            <button class="nav-link" data-toggle="tab" href="#{{i['id']}}-prof" aria-controls="escola-do-rock-prof" aria-selected="false">Escolas</button>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- aqui começa o conteudo das guias  -->
            <div class="tab-content">
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
                                        <input type="text" placeholder="Escola do rock" class="form-control disabled{{i['id']}} " size="30" name="" id="nome{{i['id']}}" value="{{i['nome']}}" disabled>
                                    </div>
                                    <div class="col-md-" style="padding-left: 10px">
                                        <label for="CNPJ">CNPJ</label>
                                        <br>
                                        <input type="text" size="24" class="form-control disabled{{i['id']}} " name="" id="cnpj{{i['id']}}" value="{{i['cnpj']}}" disabled>
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
                                      <label for="gestor">gestor</label>
                                      <br>
                                        <input type="text" size="33" class="form-control disabled{{i['id']}}" name="" id="diretor{{i['id']}}" value="{{i['vinculo_gestor_rede']}}" disabled>
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
                                <div class="col-md-4" style="padding-left: 10px;padding-right: 30px;">
                                    <label for="bairro">Bairro</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="24" name="bairro" id="bairro{{i['id']}}" value="{{i['bairro']}}" disabled>
                                </div>
                            </div>
                            <div class="offset-md-1  row">
                                <div class="col-md-6">
                                    <label for="complemento">Complemento</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="50" name="endereço" id="complemento{{i['id']}}" value="{{i['complemento']}}" disabled>
                                </div>
                                <div class="col-md-6" style="padding-left: 10px;padding-right: 30px;">
                                    <label for="cep">CEP</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="32" name="cep" id="cep{{i['id']}}" value="{{i['cep']}}" disabled>
                                </div>

                            </div>
                            <div class="offset-md-1 row distanciamento">
                                <div class="col-md-6">
                                    <label for="estado">Estado</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="50" name="estado" id="estado{{i['id']}}" value="{{i['estado']}}" disabled>
                                </div>
                                <div class="col-md-6" style="padding-left: 10px ;padding-right: 30px;">
                                    <label for="municipio">Municipio</label>
                                    <input type="text" class="form-control disabled{{i['id']}}" size="32" name="municipio" id="municipio{{i['id']}}" value="{{i['municipio']}}" disabled>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
                <!-- aqui termina o conteudo da guia do dados de escola  -->
                <div class="tab-pane fade aba-prof" id="{{i['id']}}-prof" role="tabpanel" aria-labelledby="{{i['nome']}}-prof">
                    <div class="row">
                        <div class="container">
                            <div class="offset-md-1 distanciamento col-md-" style="margin-top: 20px">
                                <p>Escolas
                                    <i class="far fa-question-circle"></i>
                                </p>
                            </div>
                            % for z in i['escola']:
                                <div class="row">
                                    <div class="col-md-11">
                                        <div class="offset-md-1 nome-prof row row-impar">
                                            <div class="col-md-11">
                                                {{z['nome']}}
                                            </div>
                                            <div class="col-md-1 item-tabela">
                                                <a href="">
                                                    <i class="fas fa-edit edit-ico"></i>
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            % end
                        </div>
                    </div>
                </div>
                <br>
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
                        <span onclick="allow_edit({{i['id']}})" class="{{i['id']}}" id="icone_edit{{i['id']}}" style="cursor:pointer;">
                            <i class="fas fa-edit edit-ico" style="color: #969696;"></i>
                        </span>
                        <span onclick="update_rede({{i['id']}})" id="edit{{i['id']}}" style="cursor:pointer;display:none;">
                            <i class="far fa-save fa-lg" style="color: #969696;padding-left: 16px;"></i>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<script>
    function nao_sair_sem_salvar(id_class){
   var id = "."+id;
var $elem = $(id);

$elem.on("mouseenter", function (e) {
    e.stopImmediatePropagation();
});

$elem.tooltip({ items: id, content: "Salve meu bom"});

$elem.on("click", function (e) {

    $elem.tooltip("open");
});


$elem.on("mouseleave", function (e) {
    e.stopImmediatePropagation();
});

    }

function myFunction(id) {
    var element = document.getElementById("myDIV");
    element.classList.remove("mystyle");
}

</script>