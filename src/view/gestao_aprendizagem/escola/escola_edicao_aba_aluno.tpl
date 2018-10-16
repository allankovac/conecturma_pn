<div class="row">

    <button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#cadastroaluno{{i['id']}}" style="position: absolute; right: 71px; top: 75px;">
        + Novo Aluno
    </button>

    <div class="container">
        <div class="offset-md-1 distanciamento col-md-" style="margin-top: 41px;">

        </div>
        % for z in i['aluno']:
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
        %end
    </div>
</div>
