%include('gestao_aprendizagem/header/header.tpl', title="Gestão Aprendizagem", css="relatorio_aluno.css")
%include('gestao_aprendizagem/menu/menu.tpl')

<div class="col-md-9 order-md-2" style="margin-top: 6px;">
    <div class="col-md text-rel" style="padding-left:0px;">
        <h2>Selecione o Aluno</h2>
    </div>

    <table class="table table-bordered" style="margin-top:0;">
    <thead style="background-color:#9ed0f6;">
      <tr style="color:#fff;">
        <th scope="col">Nome</th>
        <th scope="col">Turma</th>
      </tr>
    </thead>

    <tbody style="background-color:#f3f3f3;">
        % for i in alunos:
          <tr style="cursor: pointer;" onclick="redirect_vizualizar_relatorio({{i['id']}})">
            <td>{{i['nome']}}</td>
            <td>{{i['vinculo_turma']}}</td>
          </tr>
        % end
    </tbody>
  </table>

</div>
<script>
    function redirect_vizualizar_relatorio(id){
        window.location.replace("/relatorios/visualizar_relatorio_aluno?aluno="+id);
    }

</script>
    </div>
</div>

<!--<footer class="text-muted footer1">
    <div class="footer-font">Política de Privacidade | Copyright &copy; Aondê Educacional</div>
</footer>-->
<script type="text/javascript" src="../static/js/jquery-3.3.1-min.js"></script>
<script type="text/javascript" src="../static/js/Chart.min.js"></script>
<script type="text/javascript" src="../static/js/bootstrap.bundle.min.js"></script>
<script type="text/javascript" src="../static/js/bootstrap.min.js"></script>
<script type="text/javascript" src="../static/js/graficoRelatorio.js"></script>

%include('gestao_aprendizagem/footer/footer.tpl')
