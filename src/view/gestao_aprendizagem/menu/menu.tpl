% if tipo == '3':
<div class="row" style="margin-right: 0px;margin-top:20px;">
        <div class="col-md-3 order-md-1" style="margin-top: 15px;">
        <div>
            <a href="/gestao_aprendizagem" class="home-font" >
                <p class="list-group-item home-background">
                        <span style="margin-left: 56px">
                                Home
                        </span>
                </p>
            </a>
            <div class="list-group-item relatorios">
                <img class="mr-2 relatorio-ico" src="/static/img/relatorios_ico.png">
                Relatórios
            </div>
            <div align="left">
            
            <a href="/relatorios/aluno" class="list-group-item li-background"><span style="margin-left: 54px;">Desempenho de aluno</span></a>
            <!--<a href="#" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da turma</span></a>-->

            </div>
            <div class="list-group-item  gerenc-cadastro">
                <div class="row">
                    <img src="/static/img/cadastros_ico.png" class="cadastros-ico">
                    <div style="margin-left: .5rem;" class="row">
                        Gerenciamento de<br>Cadastro
                    </div>

                </div>

            </div>
            <div align="left">
                
                    <a href="/turma" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Turma</span></a>
                    <a href="/gestao_aprendizagem/usuario" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Usuário</span></a>
               
            </div>

            <a class="list-group-item recursos-ped recursos-ped-background" href="#"> <img src="/static/img/recursos_ico.png" class="mr-2 recursos-ico"> Recursos pedagogicos</a>

        </div>
    </div>

% elif tipo == '2':
<div class="row" style="margin-right: 0px;margin-top:20px">
    <div class="col-md-3 order-md-1" style="margin-top: 15px;">
    <div>
        <a href="/gestao_aprendizagem" class="home-font" >
            <p class="list-group-item home-background">
                    <span style="margin-left: 56px">
                            Home
                        </span>
            </p>
        </a>
        <div class="list-group-item relatorios">
            <img class="mr-2 relatorio-ico" src="/static/img/relatorios_ico.png">
            Relatórios
        </div>
        <div align="left">
        
                <a href="/relatorios/aluno" class="list-group-item li-background"><span style="margin-left: 54px;">Desempenho de aluno</span></a>
                <!--<a href="#" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da turma</span></a>
                <a href="#" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da escola</span></a>-->
        </div>
        <div class="list-group-item  gerenc-cadastro">
            <div class="row">
                <img src="/static/img/cadastros_ico.png" class="cadastros-ico">
                <div style="margin-left: .5rem;" class="row">
                    Gerenciamento de<br>Cadastro
                </div>

            </div>

        </div>
        <div align="left">
                <a href="/escola" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Escola</span></a>
                <a href="/turma" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Turma</span></a>
                <a href="/gestao_aprendizagem/usuario" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Usuário</span></a>
        </div>

        <a class="list-group-item recursos-ped recursos-ped-background" href="#"> <img src="/static/img/recursos_ico.png" class="mr-2 recursos-ico"> Recursos pedagogicos</a>

    </div>
</div>
% elif tipo == '1':
<div class="row" style="margin-right: 0px;margin-top:20px">
    <div class="col-md-3 order-md-1" style="margin-top: 15px;">
    <div>
        <a href="/gestao_aprendizagem" class="home-font" >
            <p class="list-group-item home-background">
                    <span style="margin-left: 56px">
                            Home
                        </span>
            </p>
        </a>
        <div class="list-group-item relatorios">
            <img class="mr-2 relatorio-ico" src="/static/img/relatorios_ico.png">
            Relatórios
        </div>
        <div align="left">
        
                <a href="/relatorios/aluno" class="list-group-item li-background"><span style="margin-left: 54px;">Desempenho de aluno</span></a>
                <!--<a href="#" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da turma</span></a>
                <a href="#" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da escola</span></a>
                <a href="#" class="list-group-item li-background justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da Rede</span></a>-->
        </div>
        <div class="list-group-item  gerenc-cadastro">
            <div class="row">
                <img src="/static/img/cadastros_ico.png" class="cadastros-ico">
                <div style="margin-left: .5rem;" class="row">
                    Gerenciamento de<br>Cadastro
                </div>

            </div>

        </div>
        <div align="left">
                <a href="/rede" class="list-group-item li-background  justify-content-between li-background lh-condensed" ><span style="margin-left: 54px;">Rede</span></a>
                <a href="/escola" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Escola</span></a>
                <a href="/turma" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Turma</span></a>
                <a href="/gestao_aprendizagem/usuario" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Usuário</span></a>
        </div>

        <a class="list-group-item recursos-ped recursos-ped-background" href="#"> <img src="/static/img/recursos_ico.png" class="mr-2 recursos-ico"> Recursos pedagogicos</a>

    </div>
</div>
% elif tipo == '0':
<div class="row" style="margin-right: 0px;margin-top: 20px;">
    <div class="col-md-3 order-md-1" style="margin-top: 15px;">
    <div>
        <a href="/gestao_aprendizagem" class="home-font" >
            <p class="list-group-item home-background">
                <span style="margin-left: 56px">
                    Home
                </span>
            </p>
        </a>
        <div class="list-group-item relatorios">
            <img class="relatorio-ico" src="/static/img/relatorios_ico.png">
            Relatórios
        </div>
        <div align="left">
        
            <a href="/relatorios/aluno" class="list-group-item li-background"><span style="margin-left: 54px;">Desempenho de aluno</span></a>
            <!--<a href="#" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da turma</span></a>
            <a href="#" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da escola</span></a>
            <a href="#" class="list-group-item li-background justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da Rede</span></a>-->
        </div>
        <div class="list-group-item  gerenc-cadastro">
            <div class="row">
                <img src="/static/img/cadastros_ico.png" class="cadastros-ico">
                <div style="margin-left: 16px;" class="row">
                    Gerenciamento de<br>Cadastro
                </div>

            </div>

        </div>
        <div align="left">
            <a href="/rede" class="list-group-item li-background  justify-content-between li-background lh-condensed" ><span style="margin-left: 54px;">Rede</span></a>
            <a href="/escola" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Escola</span></a>
            <a href="/turma" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Turma</span></a>
            <a href="/gestao_aprendizagem/usuario" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Usuário</span></a>
        </div>

        <a class="list-group-item recursos-ped recursos-ped-background" href="/recurso"> <img src="/static/img/recursos_ico.png" class="mr-2 recursos-ico"> Recursos pedagogicos</a>
    </div>
</div>
% elif tipo == '2.5':
<div class="row" style="margin-right: 0px;margin-top: 20px;">
    <div class="col-md-3 order-md-1" style="margin-top: 15px;">
    <div>
        <a href="/gestao_aprendizagem" class="home-font" >
            <p class="list-group-item home-background">
                <span style="margin-left: 56px">
                    Home
                </span>
            </p>
        </a>
        <div class="list-group-item relatorios">
            <img class="relatorio-ico" src="/static/img/relatorios_ico.png">
            Relatórios
        </div>
        <div align="left">

            <a href="/relatorios/aluno" class="list-group-item li-background"><span style="margin-left: 54px;">Desempenho de aluno</span></a>
            <!--<a href="#" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Desempenho da turma</span></a>-->
        </div>
        <div class="list-group-item  gerenc-cadastro">
            <div class="row">
                <img src="/static/img/cadastros_ico.png" class="cadastros-ico">
                <div style="margin-left: 16px;" class="row">
                    Gerenciamento de<br>Cadastro
                </div>

            </div>

        </div>
        <div align="left">
            <a href="/turma" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Turma</span></a>
            <a href="/gestao_aprendizagem/usuario" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Usuário</span></a>
        </div>

        <a class="list-group-item recursos-ped recursos-ped-background" href="#"> <img src="/static/img/recursos_ico.png" class="mr-2 recursos-ico"> Recursos pedagogicos</a>
    </div>
</div>
% elif tipo == '4':
<div class="row" style="margin-right: 0px;margin-top: 20px;">
    <div class="col-md-3 order-md-1" style="margin-top: 15px;">
    <div>
        <a href="/gestao_aprendizagem" class="home-font" >
            <p class="list-group-item home-background">
                <span style="margin-left: 56px">
                    Home
                </span>
            </p>
        </a>
        <div class="list-group-item relatorios">
            <img class="relatorio-ico" src="/static/img/relatorios_ico.png">
            Relatórios
        </div>
        <div align="left">
            <a href="/relatorios/aluno" class="list-group-item li-background"><span style="margin-left: 54px;">Desempenho de aluno</span></a>
        </div>
        <div class="list-group-item  gerenc-cadastro">
            <div class="row">
                <img src="/static/img/cadastros_ico.png" class="cadastros-ico">
                <div style="margin-left: 16px;" class="row">
                    Gerenciamento de<br>Cadastro
                </div>

            </div>

        </div>
        <div align="left">
            <a href="/gestao_aprendizagem/usuario" class="list-group-item li-background  justify-content-between li-background lh-condensed"><span style="margin-left: 54px;">Usuário</span></a>
        </div>

        <a class="list-group-item recursos-ped recursos-ped-background" href="#"> <img src="/static/img/recursos_ico.png" class="mr-2 recursos-ico"> Recursos pedagogicos</a>
    </div>
</div>


