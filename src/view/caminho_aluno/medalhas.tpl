<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Sala de Medalhas</title>
    <link rel="stylesheet" href="../static/bootstrap.min.css">
    <link rel="stylesheet" href="../static/medalhas.css">
    <link rel="icon" type="image/png" href="../static/img/icon_conecturma.png">
    <script type="text/javascript" src="../static/js/jquery-3.3.1-min.js"></script>
    <script type="text/javascript" src="../static/js/bootstrap.min.js"></script>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

</head>

<body>
<header>
    <div style="zindex" class="container cabecalho">
        <div class="row">
            <div class="menu col-md-9 offset-md-2">
                <ul>
                    <li class="c"><a href="/aluno/area_aluno"></a> </li>
                    <li class="ambiente"><a href="/gestao_aprendizagem"></a></li>
                    <li class="facebook offset-md-1"><a href="https://www.facebook.com/conecturmaoficial/"
                                                        target="_blank"></a></li>
                    <li class="youtube offset-md-1"><a href="https://www.youtube.com/conecturma" target="_blank"></a>
                    </li>
                    <li class="sair offset-md-1"><a href="/sair"></a></li>
                </ul>
            </div>
        </div>
    </div>
</header>

<main>
    <div class="container offset-md-2">
        <div style="margin-left: 11px;">
            <div class="titulo" style="margin-top: 30px;margin-left: -17px;"></div>


            <br>
            %if (medalha_recente):
            <div style="margin-left: -14px;"><img src="/static/img/medalha/recentes.png"></div>
        </div>

        <div class="col-md">
            <br>
            <br>
            <div class="row">

                % for i in medalha_recente:
                    %if i['tipo_medalha']== '2' :
                        <div class="bounce" style="background-image: url('/static/img/medalha/fundo-medalha-recente.png');width: 220px;height:220px;text-align: center;display: block;opacity: 1; margin-left:0px;margin-right:10px;">
                            <figure>
                                <img class="medalha-lista-ultimas" src="/static/img/medalha/jogo-{{i['id']}}.png">
                            </figure>
                        </div>

                    %else:
                        <div class="bounce" style=" background-image: url('/static/img/medalha/fundo-medalha-recente.png');width: 220px;height:220px;text-align: center;display: block;opacity: 1; margin-left:0px;margin-right:10px;">

                            <figure>
                                <img class="medalha-lista-ultimas" src="/static/img/medalha/socio/socio-{{i['id']}}.png">
                            </figure>
                        </div>
                    %end
                %end
            </div>
            %end



        </div>


        <img src="/static/img/medalha/separador.png" align="center"
             style="top: 20px;position: relative; margin-left: auto; margin-right:auto;">


        <br>
        <br>
        <br>


        <div class="row" style="margin-left: -3px;">
            <div class="col-md-3">
                <img src="/static/img/medalha/medalhas.png" style="margin-left: -13px;">
            </div>

            <ul class="nav nav-pills mb-3 nav-botoes" id="pills-tab" role="tablist">
                <li class="nav-item">
                    <a class="nav-link active" id="pills-home-tab" data-toggle="pill" href="#pills-home" role="tab"
                       aria-controls="pills-home" aria-selected="true"
                       style="text-transform:uppercase;border-radius:10px;">Desempenho</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" id="pills-profile-tab" data-toggle="pill" href="#pills-profile" role="tab"
                       aria-controls="pills-profile" aria-selected="false"
                       style="margin-left:20px;text-transform:uppercase;border-radius: 10px;">SócioEmocional</a>
                </li>

            </ul>
        </div>
        <div class="tab-content" id="pills-tabContent" style="width:990px;">
            <div class="tab-pane fade show active" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">

                <div class="todas-medalhas">
                    <div class="row col-md-11" style="padding-left: 32px;">

                        % for i in medalha_jogo:
                            %if usuario['tipo'] < '6':
                        <div class="todasmedalhas bounce"
                             style="background-image: url('/static/img/medalha/fundo-medalha-todas.png');width: 150px;height: 150px;text-align: center;margin: 10px -8px 10px 30px;display: block;opacity: 1;">
                            <img alt="Jogador " class="medalha-lista-todas" data-id="" data-imagem=""
                                 id="{{i['id']}}"
                                 src="/static/img/medalha/jogo-{{i['id']}}.png" style="">
                        </div>
                            %elif usuario['tipo'] >='6':
                                % if str(i['id']) in medalha_aluno:
                        <div class="todasmedalhas bounce"
                             style="background-image: url('/static/img/medalha/fundo-medalha-todas.png');width: 150px;height: 150px;text-align: center;margin: 10px -8px 10px 30px;display: block;opacity: 1;">
                            <img alt="Jogador " class="medalha-lista-todas" data-id="" data-imagem=""
                                 id="{{i['id']}}"
                                 src="/static/img/medalha/jogo-{{i['id']}}.png" style="">
                        </div>
                                %else:
                        <div class="todasmedalhas bounce"
                             style="background-image: url('/static/img/medalha/fundo-medalha-todas.png');width: 150px;height: 150px;text-align: center;margin: 10px -8px 10px 30px;display: block;opacity: 1;">
                            <img alt="Jogador " class="medalha-lista-todas" data-id="" data-imagem=""
                                 id="{{i['id']}} "
                                 src="/static/img/medalha/jogo-{{i['id']}}.png"
                                 style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">
                        </div>
                                %end

                            %end

                        %end

                    </div>

                </div>
            </div>
            <div class="tab-pane fade" id="pills-profile" role="tabpanel" aria-labelledby="pills-profile-tab">
                <div class="todas-medalhas">
                    <div class="row col-md-11" style="padding-left: 32px;">

                        % for i in medalha_socio:
                            %if usuario['tipo'] < '6':

                             <div class="todasmedalhas bounce"
                             style="background-image: url('/static/img/medalha/fundo-medalha-todas.png');width: 150px;height: 150px;text-align: center;margin: 10px -8px 10px 30px;display: block;opacity: 1;">
                                <img alt=" " class="medalha-lista-todas" data-id="" data-imagem=""
                                 id="{{i['id']}}"
                                 src="/static/img/medalha/socio/socio-{{i['id']}}.png"
                                 style="">

                        </div>
                            %else:
                                    % if str(i['id']) in medalha_aluno:

                        <div class="todasmedalhas bounce"
                             style="background-image: url('/static/img/medalha/fundo-medalha-todas.png');width: 150px;height: 150px;text-align: center;margin: 10px -8px 10px 30px;display: block;opacity: 1;">
                            <img alt=" " class="medalha-lista-todas" data-id="" data-imagem=""
                                 id="{{i['id']}}"
                                 src="/static/img/medalha/socio/socio-{{i['id']}}.png" style="">
                        </div>
                                %else:
                        <div class="todasmedalhas bounce"
                             style="background-image: url('/static/img/medalha/fundo-medalha-todas.png');width: 150px;height: 150px;text-align: center;margin: 10px -8px 10px 30px;display: block;opacity: 1;">
                            <img alt=" " class="medalha-lista-todas" data-id="" data-imagem=""
                                 id="{{i['id']}}"
                                 src="/static/img/medalha/socio/socio-{{i['id']}}.png"
                                 style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">

                        </div>
                                %end
                            %end
                        %end

                    </div>
                </div>
            </div>
        </div>
        <br>
    </div>

    <!-- POP PARABENS -->
        <div id="pop">
            <a href="#" onclick="document.getElementById('pop').style.display='none';"><img  id="fechar"src="x.png"></a>
            <br/>
            <img id="parabens" src="parabens.png">
            <br>
            <img style="width: 190px;height: auto; margin-left: 75px;" src="img/eu-penso-eu-consigo.jpg">

        </div>

</main>

<script type="text/javascript" src="../static/js/jquery-3.3.1-min.js"></script>
<script type="text/javascript">

    $(function(){

       $("*[alt=Jogador]").hover(function(e){
             var title = $(this).attr('title');
             $(this).data('titleText', title).removeAttr('title');
             $("main").append('<div class="tooltip">'+title+'</div>');

        })
             $('.tooltip').css({
                         top : e.pageY - 50,
                         left : e.pageX + 20
                         }).fadeIn();

       }, function(){
          $(this).attr('title', $(this).data('titleText'));
          $('.tooltip').remove();
       }).mousemove(function(e){
          $('.tooltip').css({
                         top : e.pageY - 50,
                         left : e.pageX + 20
                         })
       })

    });
</script>
</body>

</html>