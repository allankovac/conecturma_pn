%include('gestao_aprendizagem/header/header.tpl', title="Gestão Aprendizagem", css="css-listagem-escolas.css")
%include('gestao_aprendizagem/menu/menu.tpl')
<div class="col-md-9 order-md-3 botao-tabela" style="margin-top: 6px;">
  <div style="left: -14px;margin-bottom: 30px;position: relative;">
    <p class="top-escolas-tabela">Turma</p>
    % if tipo < '2':
    <button type="button" class="botao-nova-escola" onclick="document.getElementById('new_school').style.display = 'inline'">
      <i class="fas fa-plus"></i>
      &nbsp;Nova Turma
    </button>
    % end
  </div>

  %if tipo != '3':
  <div id="new_school" style="display:none;">
    %include('gestao_aprendizagem/turma/formulario_cadastro_nova_turma.tpl')
  </div>
  %end
  <div id="accordion">
    <!-- inicio da tabela -->

    <div class="row">
      <div class="col-md-12 item-tabela topo-tab">
        Turma
      </div>
    </div>
    <!-- bloco de cabeçalho da lista -->
    % if isinstance(turma,list):

    % for index,i in enumerate(turma):
      % if index % 2 ==0:
        <div class="row row-par">
          %include('gestao_aprendizagem/turma/turma_edicao_par.tpl')
        </div>
      % else:
        <div class="row row-impar">
          <input type="hidden" id ="id_escola" value="{{i['id']}}">
          %include('gestao_aprendizagem/turma/turma_edicao_par.tpl')
        </div>
      % end
    % end

    % else:
    <h2>Você não está cadastrado a nenhuma turma.</h2>
    % end
  </div>
</div>
</div>
<script type="text/javascript" src="../static/js/jquery-3.3.1-min.js"></script>
<script type="text/javascript">

  function test(ide) {
    console.log(ide);
    y = document.getElementById(ide).innerHTML;
    x = document.getElementById("nova-escola").style.display;
    console.log(x, y)
    if (x == "none") {
      document.getElementById("nova-escola").style.display = 'block';
      document.getElementById(ide).innerHTML = '<i class="fas fa-angle-up"></i>';
    }
    else {
      document.getElementById("nova-escola").style.display = 'none';
      document.getElementById(ide).innerHTML = '<i class="fas fa-angle-down"></i>';
      // document.getElementById(drop).style.display='block':
    }
  }

  function seta(ide) {
    setinha = document.getElementById(ide).querySelectorAll("#setinha");
    if (setinha[0].className == 'fas fa-angle-down') {
      document.getElementById(ide).innerHTML = '<i id="setinha" class="fas fa-angle-up"></i>';
    } else {
      document.getElementById(ide).innerHTML = '<i id="setinha" class="fas fa-angle-down"></i>';
    }
  };

  function sumir() {

    $('#modal-dar-medalha').on('show.bs.modal', function () {
      $('#medalha_janela').css('display', 'none');

    });

    $('#modal-dar-medalha').on('hidden.bs.modal', function () {
      $('#medalha_janela').css('display', 'block');
    });
  }

  idMedalha = [];
  function getIdMedalha(id) {
    index = idMedalha.indexOf(id);
    index == -1 ? idMedalha.push(id) : idMedalha.splice(index, 1);
  }

  function entregarMedalha(alunoid, medalha) {
    motivo = document.getElementById("motivo"+medalha);
    $.post('/turma/entregar_medalha_aluno', { aluno: alunoid, medalha: medalha, motivo: motivo.value}, function (data) {
      if(data == '1'){
        motivo.value='';
        setTimeout(alert("Medalha foi entregue com sucesso!"), 3000);
      }
      else{
        alert("Erro, medalha não pode ser entregue.");
      }
    });
  }

  function entregarMedalhaTodos(turmaId, medalha) {
    motivo = document.getElementById("motivo"+medalha+"_todos");
    $.post('/turma/entregar_medalha_todos_alunos', { turma: turmaId, medalha: medalha, motivo: motivo.value }, function (data) {
      if(data == '1'){
        motivo.value='';
        setTimeout(alert("Medalha foi entregue com sucesso!"), 3000);
      }
      else{
        alert("Erro, medalha não pode ser entregue.");
      }
    });
  }
</script>
%include('gestao_aprendizagem/footer/footer.tpl')