%include('gestao_aprendizagem/header/header.tpl', title="Gestão Aprendizagem", css="css-listagem-escolas.css")
%include('gestao_aprendizagem/menu/menu.tpl')
<div class="col-md-9 order-md-3 botao-tabela">
    <div style="left: -14px;margin-bottom: 30px;position: relative;">
        <p class="top-escolas-tabela">Usuários</p>
        %include('gestao_aprendizagem/usuario/selecao_novo_usuario.tpl')
    </div>

    %if tipo == '3':
        <div id="4" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_aluno.tpl')
        </div>
        <div id="5" style="display:none;">
            %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_responsavel.tpl')
        </div>
    %elif tipo == '0':
        <div id="1" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_gestor.tpl')
        </div>
         <div id="2" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_diretor.tpl')
        </div>
       <div id="3" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_professor.tpl')
        </div>
       <div id="4" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_aluno.tpl')
        </div>
        <div id="5" style="display:none;">
            %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_responsavel.tpl')
        </div>
        <div id="6" style="display:none;">
            %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_coordenador.tpl')
        </div>
    %elif tipo == '1':
         <div id="2" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_diretor.tpl')
        </div>
       <div id="3" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_professor.tpl')
        </div>
       <div id="4" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_aluno.tpl')
        </div>
        <div id="5" style="display:none;">
            %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_responsavel.tpl')
        </div>
        <div id="6" style="display:none;">
            %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_coordenador.tpl')
        </div>
    %elif tipo == '2':
       <div id="3" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_professor.tpl')
        </div>
       <div id="4" style="display:none;">
          %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_aluno.tpl')
        </div>
        <div id="5" style="display:none;">
            %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_responsavel.tpl')
        </div>
        <div id="6" style="display:none;">
            %include('gestao_aprendizagem/usuario/formulario_cadastro_nova_usuario_coordenador.tpl')
        </div>
    % end


    <div id="accordion">
      <!-- inicio da tabela -->
      <div class="row">
          <div class="col-md-9 item-tabela topo-tab">
            Nome
          </div>

          <div class="col-md-3 item-tabela topo-tab">
            Tipo
          </div>

      </div>
        <%
            for index,i in enumerate(usuarios):
        %>

           %include('gestao_aprendizagem/usuario/usuario_template_edicao.tpl')
        <%
            end
        %>

      <!-- bloco de cabeçalho da lista -->
  </div>
</div>
</div>
<script type="text/javascript" src="/static/js/jquery-3.3.1-min.js"></script>
<script>


$(document).ready(function(){
    $("button#dads").click(function(){
        /*$("div#novo-gestor").toggle(100);-->*/
        console.log(this);
         if("i.fas.fa-angle-up"){
         alert('if')
        $("div#novo-gestor").hide(100);
        $("i.fas.fa-angle-up").removeClass("fa-angle-up").addClass("fa-angle-down");
       }
       else {
       alert("estou no else");
         $("div#novo-gestor").show(100);
        $("i.fas.fa-angle-down").removeClass("fa-angle-down").addClass("fa-angle-up");
       }


    });
    return false
});

$(document).ready(function(){
    $("button#prof").click(function(){
        $("div#novo-professor").toggle(100);
    });
});

$(document).ready(function(){
    $("button#coordenador").click(function(){
        $("div#novo-coordenador").toggle(100);
    });
});

$(document).ready(function(){
    $("button#diretor").click(function(){
        $("div#novo-diretor").toggle(100);
    });
});

$(document).ready(function(){
    $("button#responsavel").click(function(){
        $("div#novo-responsavel").toggle(100);
    });
});

$(document).ready(function(){
    $("button#aluno").click(function(){
        $("div#novo-aluno").toggle(100);
    });
});

</script>


%include('gestao_aprendizagem/footer/footer.tpl')