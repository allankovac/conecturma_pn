%if tipo== '0':
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="1">
    Gestor
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="2">
    Diretor
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="6">
    Coordenador Pedagógico
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="3">
    Professor
    <!--<input type="radio" aria-label="Radio button for following text input">
    Gestor-->
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="5">
    Responsável
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="4" checked>
    Aluno

%elif tipo =='1':
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="2">
    Diretor
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="6">
    Coordenador Pedagógico
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="3">
    Professor
    <!--<input type="radio" aria-label="Radio button for following text input">
    Gestor-->
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="5">
    Responsável
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="4" checked>
    Aluno

%elif tipo=='2':
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="6">
    Coordenador Pedagógico
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="3">
    Professor
    <!--<input type="radio" aria-label="Radio button for following text input">
    Gestor-->
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="5">
    Responsável
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="4" checked>
    Aluno

%elif tipo =='3':
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="5">
    Responsável
    <input name="tipo_usuario" type="radio" aria-label="Radio button for following text input" value="4">
    Aluno
    <br>
%end
<br>

%if tipo != '2.5':
    <button type="button" class="botao-nova-escola" id="new_user">
      <i class="fas fa-plus"></i>
      &nbsp;Novo Usuário
    </button>
%end

