%include('gestao_aprendizagem/header/header.tpl', title="Gestão Aprendizagem", css="css-gestao-aprendizagem.css")
<div align="center" class="col-md-12">
    <h1>Bem Vindo Administrador</h1>
    <h2>A Conecturma!</h2>
</div>
<div class="row">
    <div class="col-md-2" style="margin-top:50px;">
        <p>Gerenciamento de <br>Cadastros</p>
        <a href="/rede">REDE</a><br>
        <a href="/escola">ESCOLA</a><br>
        <a href="/turma">TURMA</a><br>
        <a href="/gestao_aprendizagem/usuario">USUÁRIOS</a><br>
        <!--<a href="/cadastro_descritor_view">DESCRITOR</a><br>
        <a href="/loja/cadastrar_item">ITENS DE AVATAR</a><br>
        <a href="/ler_medalha">MEDALHAS</a><br>
        <a href="/usuarios_inativados">INATIVADOS</a>-->
    </div>
    <div class="col-md-5" style="margin-top:50px;">
        <table class="table" style="border-collapse: collapse;">
            <tr>
                <th scope="col" style="border: 1px solid #dddddd">nome do usuario</th>
                <th scope="col" style="border: 1px solid #dddddd">acao</th>
                <th scope="col" style="border: 1px solid #dddddd">momento</th>
            </tr>
            %for i in usuario:

            <tr scope="row">

                <!--<td style="border: 1px solid #dddddd">{{i['id']}}</td>-->
                <td style="border: 1px solid #dddddd" >{{i['nome_usuario']}}</td>
                <td style="border: 1px solid #dddddd">{{i['acao']}}</td>
                <td style="border: 1px solid #dddddd">{{i['momento'].strftime("%d-%m-%Y %H:%M:%S")}}</td>
            </tr>

            %end
        </table>


    </div>
</div>

%include('gestao_aprendizagem/footer/footer.tpl')