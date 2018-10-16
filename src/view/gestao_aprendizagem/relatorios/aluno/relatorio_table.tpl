<table class="table table-bordered" style="margin-top:0;">
   <thead style="background-color:#9ed0f6;">
      <tr style="color:#fff;">


        <th scope="col" >Descritor</th>
        <th scope="col">Desempenho</th>
      </tr>
    </thead>

    <tbody style="background-color:#f3f3f3;">
        %teste = 0
        %for i in oa:
            % if teste < len(porcentagem):
            <tr style="cursor: pointer;" data-toggle="collapse" data-target=".grafico{{i['id']}}" class="accordion-toggle" onclick="funcoes('grafico{{i['id']}}',{{pontos[teste]}})">
                <td>{{i['descricao_descritor']}}</td>
                  <td>
                    %if int(porcentagem[teste]) >= 70:
                        <img src="/static/img/feed-pos.png" style="display: block; margin-left: auto; margin-right: auto">
                    %elif int(porcentagem[teste]) >= 50 and int(porcentagem[teste]) <= 69:
                        <img src="/static/img/feed-med.png" style="display: block; margin-left: auto; margin-right: auto">
                    %elif int(porcentagem[teste]) >= 0 and int(porcentagem[teste]) <= 49:
                        <img src="/static/img/feed-neg.png" style="display: block; margin-left: auto; margin-right: auto">
                    %end
                </td>
            </tr>
            <tr>

                <td  class="hiddenRow" colspan="3"> <div class="accordian-body collapse grafico{{i['id']}}">
                    <div class="col-md-12" style="margin-top: 15px;">
                        <div class="row">
                            <div class="col-md-2 offset-md-3">
                                <div class="circle" style="border: 5px solid #0099ff; border-radius: 50px; width: 78px;height:78px ;">
                                    <div style="align-items: center">
                                        <span class="number" style="margin-left: 25px;">{{vezes[teste]}}</span>
                                        <span class="word"> Vezes</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-2">
                                <div class="circle" style="border: 5px solid #0099ff; border-radius: 50px; width: 78px;height:78px ;">
                                    <div style="align-items: center">
                                        <span class="number">{{porcentagem[teste]}}</span>
                                        <span class="word"> Média</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-2">
                                <div class="circle"  style="border: 5px solid #0099ff; border-radius: 50px; width: 78px;height:78px ;">
                                    <div style="align-items: center">
                                        <span class="number">000</span>
                                        <span class="word" style="margin-left: 17px;"> Final</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                     
                <canvas id="myChart_grafico{{i['id']}}"></canvas> </div> </td>
            </tr>
          % else:
            <tr>
                <td>{{i['descricao_descritor']}}</td>
                <td></td>
            </tr>
          % end
         %teste+=1
        % end
    </tbody>

</table>