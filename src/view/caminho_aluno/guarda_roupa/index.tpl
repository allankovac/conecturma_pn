<! DOCTYPE html>
<html>
    <head>
        <title>Jogar Conecturma</title>
        <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css.map">
        <link rel="stylesheet" type="text/css" href="/static/style_loja.css">
    </head>    
    <body>
        <div class="bg_ground">
            <div class="container">
                <div class="row">
                    <div class="menu col-md-9 offset-md-2">
                        <ul>
                            <li class="c"><a href="/aluno/area_aluno"></a></li>
                            <li class="ambiente"><a href="/gestao_aprendizagem"></a></li>
                            <li class="facebook offset-md-1"><a href="https://www.facebook.com/conecturmaoficial/" target="_blank"></a></li>
                            <li class="youtube offset-md-1"><a href="https://www.youtube.com/conecturma" target="_blank"></a></li>'
                            <li class="sair offset-md-1"><a href="/sair"></a></li>
                        </ul>
                    </div>
                </div>
                <div class="row" style="margin-top: 20px;">
                    <div class="col-md-4">
                        <div class="cristais">
                            <img src="/static/img/total_cristais_loja.png">
                            <span style="    font-family: 'arial';color: #fff;text-shadow: 2px 2px #733e00;font-size: 20px;position: absolute;top: 60px;    margin-left: 38px;z-index: 50;">{{cristais}}</span>
                        </div>
                        <div class="loja_space_avatar">
                             % if apelido != '0':
                                    <input id="apelido" type="text" name="apelido" onchange="salvar_avatar();" maxlength="12" value="{{apelido}}" style="text-transform:uppercase; background-color: #e75619;font-family: 'arial';color: #fff;border: 1px solid #ff8039;border-radius: 8px;height: 45px;width: 190px;padding: 0 0;font-size: 30px;text-shadow: 2px 2px #58210a;text-align: center;position: absolute;top: 41%;margin-left: 29%;">
                                % else:
                                    <input id="apelido" type="text" name="apelido" onchange="salvar_avatar();" value="" maxlength="12" style="text-transform:uppercase; background-color: #e75619;font-family: 'arial';color: #fff;border: 1px solid #ff8039;border-radius: 8px;height: 45px;width: 190px;padding: 0 0;font-size: 30px;text-shadow: 2px 2px #58210a;text-align: center;position: absolute;top: 41%;margin-left: 29%;">
                                % end
                        </div>
                        <div class="loja_avatar">
                            <div class="avatar">
                                <div id="avatar_usuario">
                                    %if cor != '0':
                                        <img id='avatar-itens-cor' src="/static/img/body/{{cor['image_name']}}" class='avatar-itens-cor imagem-pocicao-"+color.slice(0,4)+"' style="z-index: 11; position: absolute;top: 14px;left: 5px;">
                                        <input id='avatar-itens-cor-id' type='hidden' value='{{cor["id"]}}'>
                                    %else:
                                        <img id="avatar" src="/static/img/body/avatar-naked.png">
                                        <input id='avatar-itens-cor-id' type='hidden' value='0'>
                                    %end

                                    %if rosto != '0':
                                        <img id='avatar-itens-rosto' src="/static/img/rosto/{{rosto['image_name']}}" style="z-index: 12; position: absolute; top: 37px; left: 30px;">
                                        <input id='avatar-itens-rosto-id' type='hidden' value='{{rosto["id"]}}'>
                                    %else:
                                        <input id='avatar-itens-rosto-id' type='hidden' value='0'>
                                    %end

                                    %if acessorio != '0':
                                        <img id='avatar-itens-acessorios' src="/static/img/acessorio/{{acessorio['image_name']}}" style="z-index: 13; position: absolute; top: -168px; left: -81px;">
                                        <input id='avatar-itens-acessorios-id' type='hidden' value='{{acessorio["id"]}}'>
                                    %else:
                                        <input id='avatar-itens-acessorios-id' type='hidden' value='0'>
                                    %end

                                    %if corpo != '0':
                                        <img id='avatar-itens-body' src="/static/img/corpo/2{{corpo['image_name']}}" style="z-index: 12; position: absolute;top: -165px;left: -84px;">
                                        <input id='avatar-itens-body-id' type='hidden' value='{{corpo["id"]}}'>
                                    %else:
                                        <input id='avatar-itens-body-id' type='hidden' value='0'>
                                    %end
                                </div>
                            </div>
                        </div>
                        <!--<div class="botao-editar-avatar">
                            <a href="#">
                                <img src="img/btn_voltar.png">
                            </a>
                        </div>-->
                        <!--<div class="loja-luz-nave">
                        </div>-->
                    </div>
                    <div class="col-md-8">
                        <ul class="loja-categorias" style="list-style-type: none; margin-left: -30px;">
                                <div class="row">

                                    <li id="cor" class="cores scale-bounce"><a onclick="mostrar_itens(1), scale_click('cor')" style="cursor:pointer;"></a></li>
                                    <li id="rosto" class="rosto scale-bounce" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%); background-size: 60%; position: relative; top: 11px;"><a onclick="mostrar_itens(2), scale_click('rosto')" style="cursor:pointer;"></a></li>
                                    <li id="acessorios" class="acessorios scale-bounce" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%); background-size: 60%; position: relative; top: 11px;"><a onclick="mostrar_itens(3), scale_click('acessorios')" style="cursor:pointer;"></a></li>
                                    <li id="corpo" class="scale-bounce" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%); background-size: 60%; position: relative; top: 11px;"><a onclick="mostrar_itens(4),scale_click('corpo')" style="cursor:pointer;"></a></li>

                                </div>
                        </ul>

                        <div class="loja-itens">
                            <div class="offset-md-1">
                                <div id="item-comprado-cores" class="item-comprado-cores">
                                    <div id="left_button_cor" class="left_buttom loja-page" style="display:none">
                                        <a onclick="mostrar_elementos_esquerda('cor')" style="cursor:pointer;"></a>
                                    </div>
                                    %z=0
                                    % for i in range(0, (len(cores)//3)):
                                        % if i > 0:
                                            <div id="bloco-cor-{{i+1}}" style="display:none">
                                                %for a in range(z,z+3):
                                                    <div class="itens-loja-corpo" onclick="change_avatar_color('{{cores[a]['image_name']}}','{{cores[a]['id']}}'); salvar_avatar(); check_color_cor('botao_ok_{{cores[a]['id']}}');" style="margin-left: 5px;">
                                                        <div style="position: absolute; top: 357px; margin-left: 78px;">
                                                            <img id="botao_ok_{{cores[a]['id']}}" src="/static/img/botao_ok.png" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">
                                                        </div>
                                                        <div style="padding-top: 35px; float: left; width: 100%; text-align: center;">
                                                            <img class="" src="/static/img/body/{{cores[a]['image_name']}}"  style="width: 50%;">
                                                        </div>
                                                    </div>
                                                %end
                                                % if z != (len(cores)-1):
                                                   % z +=3
                                                % end
                                            </div>
                                        % else:
                                            <div id="bloco-cor-{{i+1}}">
                                                %for a in range(z, len(cores)):
                                                    %if z < 3:
                                                        <div class="itens-loja-corpo" onclick="change_avatar_color('{{cores[a]['image_name']}}','{{cores[a]['id']}}'); salvar_avatar();check_color_cor('botao_ok_{{cores[a]['id']}}');;" style="margin-left: 5px;">
                                                            <div style="position: absolute; top: 357px; margin-left: 78px;">
                                                                <img id="botao_ok_{{cores[a]['id']}}" src="/static/img/botao_ok.png" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">
                                                            </div>
                                                            <div style="padding-top: 35px; float: left; width: 100%; text-align: center;">
                                                                <img class="" src="/static/img/body/{{cores[a]['image_name']}}"  style="width: 50%;">
                                                            </div>
                                                        </div>
                                                    %else:
                                                        %break
                                                    %end
                                                    % z+=1
                                                %end
                                            </div>
                                        % end
                                    % end
                                    <div id="right_button_cor" class="right_button loja-page">
                                        <a onclick="mostrar_elementos_direita('{{ len(cores) }}', 'cor')" style="cursor:pointer;"></a>
                                    </div>
                                </div>
                                <div id="item-comprado-rosto" class="item-comprado-acessorios" style="display:none;">
                                    <div id="left_button_rosto" class="left_buttom loja-page" style="display:none">
                                        <a onclick="mostrar_elementos_esquerda('rosto')" style="cursor:pointer;"></a>
                                    </div>
                                    %z=0
                                    % for i in range(0, (len(rostos)//3)):
                                        % if i > 0:
                                            <div id="bloco-rosto-{{i+1}}" style="display:none">
                                                %for a in range(z,z+3):
                                                    <div class="itens-loja-corpo" onclick="change_avatar_face('{{rostos[a]['image_name']}}','{{rostos[a]['id']}}'); salvar_avatar();check_color_rosto('botao_ok_{{rostos[a]['id']}}');" style="margin-left: 5px;">
                                                        <div style="position: absolute; top: 357px; margin-left: 78px;">
                                                                <img id="botao_ok_{{rostos[a]['id']}}" src="/static/img/botao_ok.png" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">
                                                        </div>
                                                        <div style="padding-top: 60px; float: left; width: 100%; text-align: center;">
                                                            <img class="rosto" src="/static/img/rosto/{{rostos[a]['image_name']}}" style="width: 50%;">
                                                        </div>
                                                    </div>
                                                %end
                                                % if z != (len(rostos)-1):
                                                   % z +=3
                                                % end
                                            </div>
                                        % else:
                                            <div id="bloco-rosto-{{i+1}}">
                                                %for a in range(z, len(rostos)):
                                                    %if z < 3:
                                                        <div class="itens-loja-corpo" onclick="change_avatar_face('{{rostos[a]['image_name']}}','{{rostos[a]['id']}}'); salvar_avatar(); check_color_rosto('botao_ok_{{rostos[a]['id']}}');" style="margin-left: 5px;">
                                                            <div style="position: absolute; top: 357px; margin-left: 78px;">
                                                                <img id="botao_ok_{{rostos[a]['id']}}" src="/static/img/botao_ok.png" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">
                                                            </div>
                                                            <div style="padding-top: 60px; float: left; width: 100%; text-align: center;">
                                                                <img class="rosto" src="/static/img/rosto/{{rostos[a]['image_name']}}" style="width: 50%;">
                                                            </div>
                                                        </div>
                                                    %else:
                                                        %break
                                                    %end
                                                    % z+=1
                                                %end
                                            </div>
                                        % end
                                    % end
                                    <div id="right_button_rosto" class="right_button loja-page">
                                        <a onclick="mostrar_elementos_direita('{{ len(rostos) }}', 'rosto')" style="cursor:pointer;"></a>
                                    </div>
                                </div>

                                <div id="item-comprado-acessorios" class="item-comprado-acessorios" style="display:none;">
                                    <div id="left_button_acessorio" class="left_buttom loja-page" style="display:none">
                                        <a onclick="mostrar_elementos_esquerda('acessorio')" style="cursor:pointer;"></a>
                                    </div>
                                    %z=0
                                    % for i in range(0, (len(acessorios)//3)):
                                        % if i > 0:
                                            <div id="bloco-acessorio-{{i+1}}" style="display:none">
                                                %for a in range(z,z+3):
                                                    <div class="itens-loja-corpo" style="margin-left: 5px;">
                                                        % if str(acessorios[a]['id']) in itens_usuario or usuario_logado['tipo']<= '5':
                                                            <div style="float: left; width: 100%; text-align: center;" onclick="change_avatar_acessorios('{{acessorios[a]['image_name']}}','{{acessorios[a]['id']}}'); salvar_avatar(); check_color_acessorios('botao_ok_{{acessorios[a]['id']}}');">
                                                                <div style="position: absolute; top: 357px; margin-left: 78px;">
                                                                    <img id="botao_ok_{{acessorios[a]['id']}}" src="/static/img/botao_ok.png" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">
                                                                </div>
                                                                <img class="acessorio" src="/static/img/acessorio/{{acessorios[a]['image_name']}}" style="max-height: 222px; margin-top: 6px;">
                                                            </div>
                                                        % else:
                                                            <div style="float: left; width: 100%; text-align: center;">
                                                                <img class="acessorio" src="/static/img/acessorio/{{acessorios[a]['image_name']}}" style="max-height: 222px; margin-top:-36px;">
                                                            </div>
                                                            <div id="setinha-{{acessorios[a]['id']}}">

                                                            </div>
                                                            <div id="buy-{{acessorios[a]['id']}}">
                                                                <div style="position: relative; margin-left: 35px;">
                                                                <img src="/static/img/custo_cristais.png" style="margin-top: -25px;">
                                                                </div>
                                                                <div style="top: -50px; float: left; position: relative; padding-left: 110px;" class="custo-cristais-loja">
                                                                    {{acessorios[a]['preco']}}
                                                                </div>
                                                                <a onclick="comprar_acessorio('{{acessorios[a]['id']}}', 3, '{{acessorios[a]['image_name']}}','{{acessorios[a]['id']}}')" style="cursor: pointer; position: relative; margin-left: 44px; float: left;top: -26px;">
                                                                    <img src="/static/img/btn_comprar.png">
                                                                </a>
                                                            </div>

                                                        %end
                                                    </div>
                                                %end
                                                % if z != (len(rostos)-1):
                                                   % z +=3
                                                % end
                                            </div>
                                        % else:
                                            <div id="bloco-acessorio-{{i+1}}">
                                                %for a in range(z, len(acessorios)):
                                                    %if z < 3:
                                                        <div class="itens-loja-corpo" style="margin-left: 5px;">
                                                            % if str(acessorios[a]['id']) in itens_usuario or usuario_logado['tipo']<= '5':
                                                                <div style="float: left; width: 100%; text-align: center;" onclick="change_avatar_acessorios('{{acessorios[a]['image_name']}}','{{acessorios[a]['id']}}'); salvar_avatar(); check_color_acessorios('botao_ok_{{acessorios[a]['id']}}');">
                                                                    <div style="position: absolute; top: 357px; margin-left: 78px;">
                                                                        <img id="botao_ok_{{acessorios[a]['id']}}" src="/static/img/botao_ok.png" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">
                                                                    </div>
                                                                    <img class="acessorio" src="/static/img/acessorio/{{acessorios[a]['image_name']}}" style="max-height: 222px; margin-top: 6px;">
                                                                </div>
                                                            % else:

                                                                <div style="float: left; width: 100%; text-align: center;">
                                                                    <img class="acessorio" src="/static/img/acessorio/{{acessorios[a]['image_name']}}" style="max-height: 222px; margin-top:-36px;">
                                                                </div>
                                                                <div id="setinha-{{acessorios[a]['id']}}">

                                                                </div>
                                                                <div id="buy-{{acessorios[a]['id']}}">
                                                                    <div style="position: relative; margin-left: 35px;">
                                                                    <img src="/static/img/custo_cristais.png" style="margin-top: -25px;">
                                                                    </div>
                                                                    <div style="top: -50px; float: left; position: relative; padding-left: 110px;" class="custo-cristais-loja">
                                                                        {{acessorios[a]['preco']}}
                                                                    </div>
                                                                    <a onclick="comprar_acessorio('{{acessorios[a]['id']}}', 3, '{{acessorios[a]['image_name']}}','{{acessorios[a]['id']}}')" style="cursor: pointer; position: relative; margin-left: 44px; float: left;top: -26px;">
                                                                        <img src="/static/img/btn_comprar.png">
                                                                    </a>
                                                                </div>

                                                            %end
                                                        </div>
                                                    %else:
                                                        %break
                                                    %end
                                                    % z+=1
                                                %end
                                            </div>
                                        % end
                                    % end
                                    <div id="right_button_acessorio" class="right_button loja-page">
                                        <a onclick="mostrar_elementos_direita('{{ len(acessorios) }}', 'acessorio')" style="cursor:pointer;"></a>
                                    </div>
                                </div>

                                <div id="item-comprado-corpo" class="item-comprado-acessorios" style="display:none;">
                                    <div id="left_button_corpo" class="left_buttom loja-page" style="display:none">
                                        <a onclick="mostrar_elementos_esquerda('corpo')" style="cursor:pointer;"></a>
                                    </div>
                                    %z=0
                                    % for i in range(0, (len(corpos)//3)):
                                        % if i > 0:
                                            <div id="bloco-corpo-{{i+1}}" style="display:none">
                                                %for a in range(z,z+3):
                                                    <div class="itens-loja-corpo" style="margin-left: 5px;">
                                                        % if str(corpos[a]['id']) in itens_usuario or usuario_logado['tipo']<= '5':
                                                            <div style="padding-top: 35px; float: left; width: 100%; text-align: center;" onclick="change_avatar_body('{{corpos[a]['image_name']}}','{{corpos[a]['id']}}'); salvar_avatar(); check_color_corpo('botao_ok_{{corpos[a]['id']}}');">
                                                                <div style="position: absolute; top: 357px; margin-left: 78px;">
                                                                    <img id="botao_ok_{{corpos[a]['id']}}" src="/static/img/botao_ok.png">
                                                                </div>
                                                                <img class="acessorio" src="/static/img/corpo/{{corpos[a]['image_name']}}" style="width: 50%;">
                                                            </div>
                                                        %else:
                                                            <div style="padding-top: 29px; float: left; width: 100%; text-align: center;">
                                                                <img class="acessorio" src="/static/img/corpo/{{corpos[a]['image_name']}}" style="width: 50%;">
                                                            </div>
                                                            <div id="setinha-{{corpos[a]['id']}}">

                                                            </div>
                                                            <div id="buy-{{corpos[a]['id']}}" style="margin-top: 117px;">
                                                                <div style="position: relative; margin-left: 35px;">
                                                                    <img src="/static/img/custo_cristais.png" style="margin-top: 41px;">
                                                                </div>
                                                                <div style="top: -50px; float: left; position: relative; padding-left: 110px;" class="custo-cristais-loja">
                                                                    {{corpos[a]['preco']}}
                                                                </div>

                                                                <a onclick="comprar_acessorio('{{corpos[a]['id']}}', 4, '{{corpos[a]['image_name']}}','{{corpos[a]['id']}}')" style="cursor: pointer; position: relative; margin-left: 44px; float: left;top: -26px;">

                                                                    <img src="/static/img/btn_comprar.png">
                                                                </a>
                                                            </div>
                                                        %end
                                                    </div>
                                                %end
                                                % if z != (len(rostos)-1):
                                                   % z +=3
                                                % end
                                            </div>
                                        % else:
                                            <div id="bloco-corpo-{{i+1}}">
                                                %for a in range(z, len(corpos)):
                                                    %if z < 3:
                                                        <div class="itens-loja-corpo" style="margin-left: 5px;">
                                                             % if str(corpos[a]['id']) in itens_usuario or usuario_logado['tipo']<= '5':
                                                                <div style="padding-top: 35px; float: left; width: 100%; text-align: center;" onclick="change_avatar_body('{{corpos[a]['image_name']}}','{{corpos[a]['id']}}'); salvar_avatar(); check_color_corpo('botao_ok_{{corpos[a]['id']}}');">
                                                                    <div style="position: absolute; top: 357px; margin-left: 78px;">
                                                                        <img id="botao_ok_{{corpos[a]['id']}}" src="/static/img/botao_ok.png" style="opacity: 0.5;grayscale(100%);-webkit-filter: grayscale(100%);">
                                                                    </div>
                                                                    <img class="acessorio" src="/static/img/corpo/{{corpos[a]['image_name']}}" style="width: 50%;">
                                                                </div>
                                                            %else:
                                                                <div style="padding-top: 29px; float: left; width: 100%; text-align: center;">
                                                                    <img class="acessorio" src="/static/img/corpo/{{corpos[a]['image_name']}}" style="width: 50%;">
                                                                </div>
                                                                <div id="setinha-{{corpos[a]['id']}}">

                                                                </div>
                                                                <div id="buy-{{corpos[a]['id']}}" style="margin-top: 117px;">
                                                                    <div style="position: relative; margin-left: 35px;">
                                                                        <img src="/static/img/custo_cristais.png" style="margin-top: 41px;">
                                                                    </div>
                                                                    <div style="top: -50px; float: left; position: relative; padding-left: 110px;" class="custo-cristais-loja">
                                                                        {{corpos[a]['preco']}}
                                                                    </div>

                                                                    <a onclick="comprar_acessorio('{{corpos[a]['id']}}', 4, '{{corpos[a]['image_name']}}','{{corpos[a]['id']}}')" style="cursor: pointer; position: relative; margin-left: 44px; float: left;top: -26px;">

                                                                        <img src="/static/img/btn_comprar.png">
                                                                    </a>
                                                                </div>
                                                            %end
                                                        </div>
                                                    %else:
                                                        %break
                                                    %end
                                                    % z+=1
                                                %end
                                            </div>
                                        % end
                                    % end
                                    <div id="right_button_corpo" class="right_button loja-page">
                                        <a onclick="mostrar_elementos_direita('{{ len(corpos) }}', 'corpo')" style="cursor:pointer;"></a>
                                    </div>
                                </div>
                            </div>
                            <div class="botoes">
                                <a href="/"  onclick="salvar_avatar()" >
                                    <img src="/static/img/btn-salvar.png" style="cursor:pointer;">
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="https://www.w3schools.com/lib/w3.js"></script>
        <script>
            aux_ac=0;
            aux_cor=0;
            aux_rosto=0;
            aux_corp=0;
            %if cor != '0':
                cor = "botao_ok_{{cor['id']}}"
                $("#"+cor).removeAttr('style');
            %end
            %if rosto != '0':
                rosto = "botao_ok_{{rosto['id']}}"
                $("#"+rosto).removeAttr('style');
            %end
            %if acessorio != '0':
                acessorio = "botao_ok_{{acessorio['id']}}"
                $("#"+acessorio).removeAttr('style');
            %end
            %if corpo != '0':
                corpo = "botao_ok_{{corpo['id']}}"
                $("#"+corpo).removeAttr('style');
            %end

            function check_color_cor(id){

                console.log('oi');
                document.getElementById(cor).style.filter = "grayscale(100%)";
                $("#"+id).removeAttr('style');
                cor=id;

            }
            function check_color_rosto(id){
                console.log('check rosto');

                if(rosto == id){
                console.log('if');
                document.getElementById(id).style.filter = "grayscale(100%)";

                    if(aux_rosto!=0){
                        console.log('if we',aux_rosto);
                        aux_rosto=0;
                         $("#"+id).removeAttr('style');
                         try{
                        var cara=document.getElementById(avatar-itens-rosto);

                        element.parentNode.removeChild(cara);
                        document.getElementById(avatar-itens-rosto).value=0;
                        }
                        catch(e){
                        console.log('eif',e);

                        }
                    }else{
                        try{
                        var cara=document.getElementById(avatar-itens-rosto-id);

                        element.parentNode.removeChild(cara);
                        }
                        catch(e){
                        console.log('eelse',e);
                        }
                        aux_rosto++
                    }
                }
                else{
                    console.log('else');
                    document.getElementById(rosto).style.filter = "grayscale(100%)";
                    $("#"+id).removeAttr('style');

                }
                rosto=id;


            }
            function check_color_acessorios(id){
                console.log(acessorio ,id);
                if(acessorio == id){
                console.log('if');
                document.getElementById(id).style.filter = "grayscale(100%)";

                    if(aux_ac!=0){
                        console.log('if we',aux_ac);
                        aux_ac=0;
                        $("#"+id).removeAttr('style');
                        var acessorio=document.getElementById(avatar-itens-acessorio-id);
                        element.parentNode.removeChild(acessorio);
                    }else{
                        var acessorio=document.getElementById(avatar-itens-acessorio-id);
                        element.parentNode.removeChild(acessorio);
                        aux_ac++;
                    }
                }
                else{
                console.log('else');
                document.getElementById(acessorio).style.filter = "grayscale(100%)";
                $("#"+id).removeAttr('style');
                }

                acessorio=id;
            }
            function check_color_corpo(id){
                console.log('check corpo');

                document.getElementById(corpo).style.filter = "grayscale(100%)";
                $("#"+id).removeAttr('style');
                corpo=id;
            }

            var display=1;
            function flag_display_none(flag){
                switch(flag){
                    case 1:
                        document.getElementById('item-comprado-cores').style.display = "none";
                        document.getElementById("cor").style.filter = "grayscale(100%)";
                        $("#cor").css({"background-size": "60%",  "position":"relative", "top": "10px"});
                        element = document.getElementById("cor");

                        $("#cor").addClass('scale-bounce1');


                        break;
                    case 2:
                        document.getElementById("rosto").style.filter = "grayscale(100%)";
                        document.getElementById('item-comprado-rosto').style.display = "none";
                        $("#rosto").css({"background-size": "60%","position":"relative", "top": "10px" });
                         $("#rosto").addClass('scale-bounce1');
                        break;
                    case 3:
                        document.getElementById("acessorios").style.filter = "grayscale(100%)";
                        document.getElementById('item-comprado-acessorios').style.display = "none";
                        $("#acessorios").css({"background-size": "60%", "position":"relative", "top": "10px"});
                         $("#acessorios").addClass('scale-bounce1');
                        break;
                    case 4:
                        document.getElementById("corpo").style.filter = "grayscale(100%)";
                        document.getElementById('item-comprado-corpo').style.display = "none";
                        $("#corpo").css({"background-size": "60%", "position":"relative", "top": "10px"});
                        $("#corpo").addClass('scale-bounce1');
                        break;
                } 
            }
            
            function mostrar_itens(tipo){
                switch(tipo){
                    case 1:
                        flag_display_none(display)
                        document.getElementById('item-comprado-cores').style.display = "inline-block";
                        $("#cor").removeClass('scale-bounce1');
                        $("#cor").removeAttr('style');
                        display = 1
                        break;
                    case 2:
                        flag_display_none(display)
                        $("#rosto").removeAttr('style');
                        $("#rosto").removeClass('scale-bounce1');
                        document.getElementById('item-comprado-rosto').style.display = "inline-block";
                        display = 2
                        break;
                    case 3:
                        flag_display_none(display)
                        $("#acessorios").removeAttr('style');
                        $("#acessorios").removeClass('scale-bounce1');
                        document.getElementById('item-comprado-acessorios').style.display = "inline-block";
                        display = 3
                        break;
                    case 4:
                        flag_display_none(display)
                        $("#corpo").removeAttr('style');
                        $("#corpo").removeClass('scale-bounce1');
                        document.getElementById('item-comprado-corpo').style.display = "inline-block";
                        display = 4
                        break; 
                }
            }    

            var bloco_visivel = 1;
            var elemento_ant = '';
            function mostrar_elementos_direita(total_elementos, elemento){
                total_blocos = parseInt(total_elementos)/3;
                if (elemento_ant != elemento){
                    elemento_ant = elemento

                    bloco_visivel = 1

                }

                if(bloco_visivel != total_blocos){
                 document.getElementById('left_button_'+elemento).style.display = 'block';
                    document.getElementById('bloco-'+ elemento+'-'+bloco_visivel).style.display = 'none';
                    document.getElementById('bloco-'+ elemento+'-'+(bloco_visivel+1)).style.display = 'block';
                    bloco_visivel ++;
                    if(bloco_visivel == total_blocos){
                        document.getElementById('left_button_'+elemento).style.display = 'block';
                    }
                }
            }

            function mostrar_elementos_esquerda(elemento){
                if(bloco_visivel >= 1){
                    document.getElementById('bloco-'+elemento+'-'+bloco_visivel).style.display = 'none';
                    document.getElementById('bloco-'+elemento+'-'+(bloco_visivel-1)).style.display = 'block';
                    document.getElementById('right_button_'+elemento).style.display = 'block';
                    bloco_visivel --;
                    if(bloco_visivel == 1){
                        document.getElementById('right_button_'+elemento).style.display = 'block';
                        document.getElementById('left_button_'+elemento).style.display = 'none';
                    }
                }
            }


             function comprar_acessorio(item, tipo, item_name, item_id){
                $.post('/comprar_item', {item:item},function(data){
                    if(data == '0'){
                        alert("você não tem moedas o suficiente");
                    }else{
                        switch(tipo){
                            case 3:
                                change_avatar_acessorios(item_name, item_id);
                                salvar_avatar();
                            case 4:
                                change_avatar_body(item_name, item_id);
                                salvar_avatar();
                        }

                        $("#buy-"+item).remove();
                        $("#setinha-"+item).append('<div style="position: absolute; top: 357px; margin-left: 78px;"><img id="botao_ok_{{corpos[a]['id']}}" src="/static/img/botao_ok.png"></div>');
                    }

                 });
            }
            function salvar_avatar(){

                try{
                                $.post('/equipar_item', {avatar_cor:document.getElementById("avatar-itens-cor-id").value,avatar_rosto:document.getElementById("avatar-itens-rosto-id").value
                ,avatar_acessorios:document.getElementById("avatar-itens-acessorios-id").value,avatar_body:document.getElementById("avatar-itens-body-id").value, apelido:document.getElementById("apelido").value},function(data){

                 });
                 }catch(e){
                 console.log('hmm  ',e);
                 }
            }
            var flag_rosto = 0;
            function change_avatar_color(color, id){
                color=color.toLowerCase();
                $("#avatar-itens-cor").remove();
                $("#avatar-itens-cor-id").remove();
                $("#avatar_usuario").append("<input id='avatar-itens-cor-id' type='hidden' value='"+id+"'><img id='avatar-itens-cor' src='/static/img/body/"+color+"' value='teste' class='avatar-itens-cor imagem-pocicao-"+color.slice(0,4)+"' style='z-index: 11;position: absolute;top: 14px;left: 5px;'>");
            }
            function change_avatar_face(face, id){
                face=face.toLowerCase();
                $("#avatar-itens-rosto").remove();
                $("#avatar-itens-rosto-id").remove();
                console.log('face',id,rosto);
                if(rosto=='botao_ok_'+id){
                    if(aux_rosto!=0){
                        $("#avatar_usuario").append("<input id='avatar-itens-rosto-id' type='hidden' value='"+id+"'><img id='avatar-itens-rosto' src='/static/img/rosto/"+face+"' class='avatar-itens-rosto imagem-pocicao-"+face.slice(0,8)+"' style='z-index: 12; position: absolute; top: 37px; left: 30px;'>");
                    }
                    }
                else{
                console.log('else change face');
                $("#avatar_usuario").append("<input id='avatar-itens-rosto-id' type='hidden' value='"+id+"'><img id='avatar-itens-rosto' src='/static/img/rosto/"+face+"' class='avatar-itens-rosto imagem-pocicao-"+face.slice(0,8)+"' style='z-index: 12; position: absolute; top: 37px; left: 30px;'>");
                }
            }
            function change_avatar_acessorios(acessorios, id){
                acessorios=acessorios.toLowerCase();
                $("#avatar-itens-acessorios").remove();
                $("#avatar-itens-acessorios-id").remove();
                console.log('face',id,rosto);
                if(acessorios=='botao_ok_'+id){
                    if(aux_ac!=0){
                        $("#avatar_usuario").append("<input id='avatar-itens-acessorios-id' type='hidden' value='"+id+"'><img id='avatar-itens-acessorios' src='/static/img/acessorio/"+acessorios+"' class='avatar-itens-acessorio imagem-pocicao-"+acessorios.slice(0,10)+"' style='z-index: 13; position: absolute;top: -168px; left: -81px;'>");
                    }
                    }
                else{
                $("#avatar_usuario").append("<input id='avatar-itens-acessorios-id' type='hidden' value='"+id+"'><img id='avatar-itens-acessorios' src='/static/img/acessorio/"+acessorios+"' class='avatar-itens-acessorio imagem-pocicao-"+acessorios.slice(0,10)+"' style='z-index: 13; position: absolute;top: -168px; left: -81px;'>");
                }
            }
            function change_avatar_body(body, id){
                body=body.toLowerCase();
                $("#avatar-itens-body").remove();
                $("#avatar-itens-body-id").remove();
                $("#avatar_usuario").append("<input id='avatar-itens-body-id' type='hidden' value='"+id+"'><img id='avatar-itens-body' src='/static/img/corpo/2"+body+"' class='avatar-itens-corpo' style='z-index: 12;position: absolute;top: -165px;left: -84px;'>");
            }

            function scale_click (id) {
                element = document.getElementById(id);
                $("#"+id).removeClass('scale-bounce')
                    element.offsetWidth = element.offsetWidth;
                $("#"+id).addClass('scale-bounce')
                    console.log("opa, coloquei");

            }
        </script>
    </body>
</html>