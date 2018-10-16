<img src="/static/img/icone-medalha-de-turma.png" type="button" class="float-right"  data-toggle="modal" data-target="#medalha_todos{{i['id']}}"
style="cursor: pointer; position: relative; bottom: 200px; margin-right: 36px;">
<div id="janela_medalhas" style="margin-top: 9px;">
    <!-- Modal -->
    <div id="janela_medalhas" style="margin-top: 9px;">
            <!-- Modal -->
        <div class="modal fade" id="medalha_todos{{i['id']}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
         <div class="modal-dialog" role="document"   style="margin: 22px 0 0 20%;">
           <div class="modal-content tamanho">
        
             <div class="modal-body">
           <table class="table table-borderless">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close" style="bottom: 13px; position: relative; left: 9px;">
                  <span aria-hidden="true">&times;</span>
                </button>
               <div class="table-head" style="margin-bottom: 10px; width: 102%">
                   <h5>Medalha</h5>
                   <h5 id="header-2">Competência</h5>
                   <h5 style="margin-left: 200px;">Comentário</h5>
        
               </div>
                 <tbody>
                    % for m in medalhas:
                       <tr>
                         <th scope="row"> <img src="/static/img/medalha/socio/socio-{{m['image_name']}}.png" style="width: 118px; height: auto;"></th>
                         <td colspan="2" position: absolute; > <div style="display: inline-flex">
                             <div class="descricao" style="width:274px;"><span>{{m['descricao_completa']}}</span></div>
                             <textarea id="motivo{{m['id']}}_todos" maxlength="140" placeholder="Máximo 140 caracteres!"></textarea></div>
                             <button type="button" class="btn btn-cor" onclick="entregarMedalhaTodos({{i['id']}}, {{m['id']}})" style="cursor: pointer;">Enviar</button>
                         </td>
                       </tr>
                    % end
                 </tbody>
             </table>
               </div>
           </div>
           </div>
        </div>
    </div>
</div>
<!-- FECHANDO O MODEL DAR MEDALHAS -->