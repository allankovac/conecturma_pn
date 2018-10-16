% if i['tipo'] == 'ALUNO':
    % if index % 2 ==0:
      <div class="row row-par">
        %include('gestao_aprendizagem/usuario/edicao_aluno/usuario_edicao_par.tpl')
      </div>
    % else:
      <div class="row row-impar">
        %include('gestao_aprendizagem/usuario/edicao_aluno/usuario_edicao_par.tpl')
      </div>
    % end
% elif i['tipo'] == 'PROFESSOR':
    % if index % 2 ==0:
      <div class="row row-par">
        %include('gestao_aprendizagem/usuario/edicao_professor/usuario_edicao_par.tpl')
      </div>
    % else:
      <div class="row row-impar">
        <input type="hidden" id ="id_escola" value="{{i['id']}}">
        %include('gestao_aprendizagem/usuario/edicao_professor/usuario_edicao_par.tpl')
      </div>
    % end
% elif i['tipo'] == 'DIRETOR':
    % if index % 2 ==0:
      <div class="row row-par">
        %include('gestao_aprendizagem/usuario/edicao_diretor/usuario_edicao_par.tpl')
      </div>
    % else:
      <div class="row row-impar">
        <input type="hidden" id ="id_escola" value="{{i['id']}}">
        %include('gestao_aprendizagem/usuario/edicao_diretor/usuario_edicao_par.tpl')
      </div>
    % end
% elif i['tipo'] == 'GESTOR':
    % if index % 2 ==0:
      <div class="row row-par">
        %include('gestao_aprendizagem/usuario/edicao_diretor/usuario_edicao_par.tpl')
      </div>
    % else:
      <div class="row row-impar">
        <input type="hidden" id ="id_escola" value="{{i['id']}}">
        %include('gestao_aprendizagem/usuario/edicao_diretor/usuario_edicao_par.tpl')
      </div>
    % end
% elif i['tipo'] == 'COORDENADOR':
    % if index % 2 ==0:
      <div class="row row-par">
        %include('gestao_aprendizagem/usuario/edicao_coordenador/usuario_edicao_par.tpl')
      </div>
    % else:
      <div class="row row-impar">
        <input type="hidden" id ="id_escola" value="{{i['id']}}">
        %include('gestao_aprendizagem/usuario/edicao_coordenador/usuario_edicao_par.tpl')
      </div>
    % end
% elif i['tipo'] == 'RESPONSAVEL':
    % if index % 2 ==0:
      <div class="row row-par">
        %include('gestao_aprendizagem/usuario/edicao_responsavel/usuario_edicao_par.tpl')
      </div>
    % else:
      <div class="row row-impar">
        <input type="hidden" id ="id_escola" value="{{i['id']}}">
        %include('gestao_aprendizagem/usuario/edicao_responsavel/usuario_edicao_par.tpl')
      </div>
    % end
% end
