<!DOCTYPE html>
<html lang="pt-br">
<head>
    <!--<meta charset="UTF-8">-->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{title}}</title>
    <link rel="icon" type="image/png" href="../static/img/icon_conecturma.png" >
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="../static/reset.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.0/css/all.css" integrity="sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt" crossorigin="anonymous">
    <link rel="stylesheet" href="../static/bootstrap.min.css">
    <link rel="stylesheet" href="../static/css-gestao-aprendizagem.css">
    <link rel="stylesheet" href="../static/{{css}}">
    <style>
        button{
            cursor: pointer;
        }
    </style>
</head>
<body>
<div id="header-content">
    <div class="container">
        <header>
        <div class="row">
            <div class="col-md-3">
                <a href="/gestao_aprendizagem">
                    <img src="/static/img/conecturma-logo.png" id="conecturma-logo" class="img img-fluid">
                </a>
            </div>
            <div class="col-md-5">
                <h1 id="header-text">Gestão de Aprendizagem</h1>
            </div>

            <div class="dropdown offset-md-1 header-dropdown">
                <div class="btn btn-info dropdown-toggle " role="button" id="dropdownMenuLink" data-toggle="dropdown" style="font-family: 'Myriad-Condlt', sans-serif; width: 159px; font-weight: bold; font-size: 12.84px; text-transform:uppercase; background-color:#1079c8;" aria-haspopup="true" aria-expanded="false">
                    ambientes
                </div>

                <div class="dropdown-menu" aria-labelledby="dropdownMenuLink" style="font-family: 'Myriad-Condlt', sans-serif; width: 159px; font-weight: bold; font-size: 12.84px; text-transform: uppercase; background-color: rgb(158, 208, 246); position: absolute; transform: translate3d(0px, 38px, 0px); top: 0px; left: 0px; will-change: transform;" x-placement="bottom-start">
                    <!--<a class="dropdown-item" href="#" style="color:#fff;">Administrativo</a>
                    <div class="dropdown-divider"></div>-->
                    <a class="dropdown-item" href="/aluno/area_aluno" style="color:#fff;">Aprendizagem</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="/sair" style="color:#fff;">Sair</a>
                </div>
            </div>
            </div>
        </div>
        </header>
    </div>
</div>
<div class="container">
