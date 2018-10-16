$("#new_user").on("click",function(){
    //bastante otimizavel , olhar depois
    var radioValue = $("input[name='tipo_usuario']:checked").val();
    $("#" + radioValue).css("display","block");

    gestor = document.getElementById('1').style;
    diretor = document.getElementById('2').style;
    professor = document.getElementById('3').style;
    aluno = document.getElementById('4').style;
    responsavel = document.getElementById('5').style;
    coordenador_ped = document.getElementById('6').style;

    if (radioValue =='1'){
    diretor.display='none';
    professor.display='none';
    aluno.display='none';
    responsavel.display='none';
    coordenador_ped.display='none';
    }
    else if(radioValue =='2') {
    gestor.display='none';
    professor.display='none';
    aluno.display='none';
    responsavel.display='none';
    coordenador_ped.display='none';
    }
    else if(radioValue =='3'){
    gestor.display='none';
    diretor.display='none';
    aluno.display='none';
    responsavel.display='none';
    coordenador_ped.display='none';
    }
    else if(radioValue =='4'){
    gestor.display='none';
    diretor.display='none';
    professor.display='none';
    responsavel.display='none';
    coordenador_ped.display='none';
    }
    else if(radioValue =='5'){
    gestor.display='none';
    diretor.display='none';
    aluno.display='none';
    professor.display='none';
    coordenador_ped.display='none';
    }
    else{
    gestor.display='none';
    diretor.display='none';
    professor.display='none';
    aluno.display='none';
    responsavel.display='none';
    }
});


function esqueci_senha(){
    email = document.getElementById('email')
    if(validar_se_email_existe(email)){
         window.location="/view_reformular_senha?email="+email.value;
    }
    else{
        document.getElementById('mensagem_erro').innerHTML='Email digitado não existe =('
    }
}

function filtro_usuario(){
   filtro_escola = document.getElementById('filtro_escola').value;
   filtro_rede = document.getElementById('filtro_rede').value;
   filtro_turma =  document.getElementById('filtro_turma').value;
   filtro_tipo_usuario =  document.getElementById('filtro_tipo_usuario').value;

   teste();

  $.post('/filtro_usuario', {escola:filtro_escola, rede:filtro_rede, turma:filtro_turma,tipo_usuario:filtro_tipo_usuario},function(data){
       $('#usuarios_sistema').html(data);


  });

  return false;
}
function teste(){
 $.post('/filtro_pesquisa', {escola:filtro_escola, rede:filtro_rede, turma:filtro_turma,tipo_usuario:filtro_tipo_usuario},function(data){
       console.log("log",data);
       $('#dropdown_filtros').html(data);
  });
}


function validar_campo_vazio(parametro){
    if(parametro.value == ''){
        document.getElementById(parametro.id).style.boxShadow = "0px 0px 12px #fe1313";
        return true;
    }
    else{
        document.getElementById(parametro.id).style.boxShadow = "0px 0px 0px #fe1313";
        return false;
    }
}

function emailValidador(id){
    var email = document.getElementById(id);
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(!email.value.match(mailformat)){
        document.getElementById(id).style.boxShadow = "0px 0px 12px #fe1313";
        return false
    }
    else{
        document.getElementById(id).style.boxShadow = "0px 0px 0px";
        return true
    }
}


function validar_se_email_existe(email){
    var retorno;
    $.ajax({
        url:    "/observador/email_existe",
        type:   "post",
        data:   {teste_email:email},
        async: false,

        success: function( data ){
            retorno = data;
        }
    });
    if(retorno == email){
        return true;
    }
    else{
        return false;
    }
}

var letras_senha = {'a':false, 'b':false, 'c':false, 'd':false, 'e':false, 'f':false, 'g':false, 'h':false, 'i':false, 'j':false, 'k':false, 'l':false};

function mudaEstado(letra){
 	var imagem = document.getElementById(letra);
 	var num = 3;
 	var selecionada = false;
 	if (!letras_senha[letra]){
 		imagem.style.background= 'rgba(229, 255, 84, 0.5)';
 		letras_senha[letra] = letra
 	}else{
 		imagem.style.background = ' rgba(113, 194, 117, 0.5)';
 		letras_senha[letra] = false
 	}
}

function mouse_in(letra){
 	var imagem = document.getElementById(letra);
  if (!letras_senha[letra]){
 	  imagem.style.background= 'rgba(229, 255, 84, 0.5)';
  }
}

function mouse_out(letra){
 	var imagem = document.getElementById(letra);
  if (!letras_senha[letra]){
 	  imagem.style.background= 'rgba(113, 194, 117, 0.5)';
  }
}




function login_aluno(){
  nome = document.getElementById('Login').value;
  senha = [];

  for (var i in letras_senha){
    if (letras_senha[i]){
      senha.push(letras_senha[i]);
    }
  }
  senha = senha.join('')
  $.post('/login/login_aluno', {aluno_login_nome:nome, aluno_senha:senha},function(data){
      console.log(data);
     window.location.replace(data);
  });
}


function login_professor(){
  email = document.getElementById('inputEmail').value;
  senha = document.getElementById('inputPassword').value;
  if (email != '' && senha !=''){
    $.post('/login/login_observador', {observador_login_email:email, observador_senha:senha},function(data){
        console.log(data);
       window.location.replace(data);
    });
  }
}

function filtro_relatorio_aluno_detalhe(teste){
    portugues = document.getElementById('portugues');
    matematica = document.getElementById('matematica');
    if (!portugues.checked){
        diciplina = '2'
    }
    else if (!matematica.checked){
        diciplina = '1'
    }
    else{
        location.reload();
    }

    $.get('/trazer_oas', {aluno:teste, diciplina:diciplina},function(data){
        $('#teste').html(data);
   });

}

function inputHandler(masks, max, event) {
    var c = event.target;
    var v = c.value.replace(/\D/g, '');
    var m = c.value.length > max ? 1 : 0;
    VMasker(c).unMask();
    VMasker(c).maskPattern(masks[m]);
    c.value = VMasker.toPattern(v, masks[m]);
}

var telMask = ['(99) 9999-9999', '(99) 9999-9999'];
var tel = document.querySelector('#telefone');
VMasker(tel).maskPattern(telMask[0]);
tel.addEventListener('input', inputHandler.bind(undefined, telMask, 13), false);

function cadastro_escola(){
    nome = document.getElementById('nome').value;
    cnpj = document.getElementById('cnpj').value;
    telefone = document.getElementById('telefone').value;
    data_de_criacao = document.getElementById('data_de_criacao').value;
    rede = document.getElementById('rede').value;
    endereco = document.getElementById('endereco').value;
    numero = document.getElementById('numero').value;
    bairro = document.getElementById('bairro').value;
    complemento = document.getElementById('complemento').value;
    cep = document.getElementById('cep').value;
    estado = document.getElementById('estado').value;
    municipio = document.getElementById('municipio').value;

    if (nome != '' && nome != null){
        if (telefone != '' && telefone != null && telefone.length >= 10){
            $.post('/escola/criar_escola', {nome:nome, cnpj:cnpj, telefone:telefone, data_de_criacao:data_de_criacao, rede:rede,
            endereco:endereco, numero:numero, bairro:bairro, complemento:complemento, cep:cep, estado:estado, municipio:municipio},function(data){
                window.location.replace(data) 
            });
         
        }
        else{
            alert('O campo telefone é obrigatório.');
            document.getElementById("telefone").style.boxShadow = "0px 0px 12px #fe1313";
        }
    }else{
        alert('O campo nome é obrigatório.');
        document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
    }
}

function update_escola(id){
    id = document.getElementById('id_escola'+id).value;
    nome = document.getElementById('nome'+id).value;
    cnpj = document.getElementById('cnpj'+id).value;
    telefone = document.getElementById('telefone'+id).value;
    rede = document.getElementById('rede'+id).value;
    endereco = document.getElementById('endereco'+id).value;
    numero = document.getElementById('numero'+id).value;
    bairro = document.getElementById('bairro'+id).value;
    complemento = document.getElementById('complemento'+id).value;
    cep = document.getElementById('cep'+id).value;
    estado = document.getElementById('estado'+id).value;
    municipio = document.getElementById('municipio'+id).value;


    if (nome != '' && nome != null){
        if (telefone != '' && telefone != null && telefone.length >= 10){
            $.post('/escola/editar_escola', {id:id, nome:nome, cnpj:cnpj, telefone:telefone, vinculo_rede:rede,
            endereco:endereco, numero:numero, bairro:bairro, complemento:complemento, cep:cep, estado:estado, municipio:municipio},function(data){
            });

            location.reload();
        }
        else{
            alert('O campo telefone é obrigatório.');
            document.getElementById("telefone").style.boxShadow = "0px 0px 12px #fe1313";
        }
    }else{
        alert('O campo nome é obrigatório.');
        document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
    }
}

function delete_estrutura(id){
    if(window.confirm("Tem certeza que deseja apagar essa escola ?")){
        $.post('/deletar_estrutura', {id:id},function(data){
        });
        location.reload();
    }
}

function cadastro_rede(){
    nome = document.getElementById('nome').value;
    cnpj = document.getElementById('cnpj').value;
    telefone = document.getElementById('telefone').value;
    endereco = document.getElementById('endereco').value;
    numero = document.getElementById('numero').value;
    bairro = document.getElementById('bairro').value;
    complemento = document.getElementById('complemento').value;
    cep = document.getElementById('cep').value;
    estado = document.getElementById('estado').value;
    municipio = document.getElementById('municipio').value;
    data_de_criacao = document.getElementById('data_de_criacao').value;
    if (nome != '' && nome != null){
        if (telefone != '' && telefone != null && telefone.length >= 10){
            $.post('/rede/criar_rede', {nome:nome, cnpj:cnpj, telefone:telefone,
            endereco:endereco, numero:numero, bairro:bairro, complemento:complemento, cep:cep, estado:estado, municipio:municipio, data_de_criacao:data_de_criacao},function(data){
                window.location.replace(data)
            });
        }
        else{
            alert('O campo telefone é obrigatório.');
            document.getElementById("telefone").style.boxShadow = "0px 0px 12px #fe1313";
        }
    }else{
        alert('O campo nome é obrigatório.');
        document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
    }
}

function update_rede(id){
    id = document.getElementById('id_escola'+id).value;
    nome = document.getElementById('nome'+id).value;
    cnpj = document.getElementById('cnpj'+id).value;
    telefone = document.getElementById('telefone'+id).value;
    endereco = document.getElementById('endereco'+id).value;
    numero = document.getElementById('numero'+id).value;
    bairro = document.getElementById('bairro'+id).value;
    complemento = document.getElementById('complemento'+id).value;
    cep = document.getElementById('cep'+id).value;
    estado = document.getElementById('estado'+id).value;
    municipio = document.getElementById('municipio'+id).value;


    if (nome != '' && nome != null){
        if (telefone != '' && telefone != null && telefone.length >= 10){
            $.post('/rede/editar_rede', {id:id, nome:nome, cnpj:cnpj, telefone:telefone,
            endereco:endereco, numero:numero, bairro:bairro, complemento:complemento, cep:cep, estado:estado, municipio:municipio},function(data){
            });
            location.reload();
        }
        else{
            alert('O campo telefone é obrigatório.');
            document.getElementById("telefone").style.boxShadow = "0px 0px 12px #fe1313";
        }
    }else{
        alert('O campo nome é obrigatório.');
        document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
    }
}


function cadastro_turma(){
    nome = document.getElementById('nome').value;
    serie = document.getElementById('serie').value;
    escola = document.getElementById('escola').value;
    data_de_criacao = document.getElementById('data_de_criacao').value;

    if (nome != '' && nome != null){
        if (serie!= '' && serie != null){
            if (escola!= '' && escola != null){
                $.post('/turma/cadastro_turma', {nome:nome, serie:serie, escola:escola, data_de_criacao:data_de_criacao},function(data){
                    window.location.replace(data)
                });
            }
            else{
                alert('O campo escola é obrigatório.');
            document.getElementById("telefone").style.boxShadow = "0px 0px 12px #fe1313";
            }

        }
        else{
            alert('O campo série é obrigatório.');
            document.getElementById("telefone").style.boxShadow = "0px 0px 12px #fe1313";
        }
    }else{
        alert('O campo nome é obrigatório.');
        document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
    }
}

function se_tem_medalha(aluno_medalha){
aluno = document.getElementById('aluno').value;
    $.POST('medalha/aluno-medalhas',{id:id},function(data){
    console.log("entrei hehe",data);
    medalu=data.aluno_medalhas

    })

}
function update_turma(id){

    id = document.getElementById('id_turma'+id).value;
    nome = document.getElementById('nome'+id).value;

    if (nome != '' && nome != null){
    console.log('testeif',nome,id);
            $.post('/turma/update_turma', {id:id, nome:nome},function(data){
            console.log("hm");
            });
            location.reload();
    }else{
        alert('O campo nome é obrigatório.');
        document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
    }
}

function cadastro_usuario_via_escola(tipo, id){
	switch(tipo){
		case 'professor':
			nome = document.getElementById(tipo+'_nome_'+id).value;
			nascimento = document.getElementById(tipo+'_nascimento_'+id).value;
			email = document.getElementById(tipo+'_email_'+id).value;
			escola = document.getElementById(tipo+'_escola_'+id).value;
			turma = document.getElementById(tipo+'_turma_'+id).value;

			if (nome != '' && nome != null){     
				if (email != '' && email != null && emailValidador(tipo+'_email_'+id)){
					if(!validar_se_email_existe(email)){
						if (escola != '' && escola != null){
							$.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, nascimento:nascimento, email:email, vinculo_escola:escola, vinculo_turma:turma},function(data){
								window.location.replace(data);
							});
							location.reload();
						}
						else{
							alert('O campo escola é obrigatório.');
							document.getElementById(tipo+'_escola').style.boxShadow = "0px 0px 12px #fe1313";
						}

					}
					else{
						alert('O email digitado já foi cadastrado no nosso sitema.');
						document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
					}
				}
				else{
					alert('O campo email é obrigatório.');
					document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
				}
			}
			else{
				alert('O campo nome é obrigatório.');
				document.getElementById(tipo+'_nome').style.boxShadow = "0px 0px 12px #fe1313";
            }
            
        case 'coordenador':
            nome = document.getElementById(tipo+'_nome_'+id).value;
            nascimento = document.getElementById(tipo+'_nascimento_'+id).value;
            email = document.getElementById(tipo+'_email_'+id).value;
            escola = document.getElementById(tipo+'_escola_'+id).value;
            $.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, nascimento:nascimento, email:email, vinculo_escola:escola},function(data){
                window.location.replace(data);
            });

        case 'aluno':
            nome = document.getElementById(tipo+'_nome_'+id).value;
            nascimento = document.getElementById(tipo+'_nascimento_'+id).value;
            sexo = document.getElementById(tipo+'_sexo_'+id).value;
            escola = document.getElementById(tipo+'_escola_'+id).value;
            turma = document.getElementById(tipo+'_turma_'+id).value;
            if (nome != '' && nome != null){
                if (escola != '' && escola != null){
                    $.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, nascimento:nascimento, sexo:sexo, vinculo_escola:escola, vinculo_turma:turma},function(data){
                        window.location.replace(data);
                    });
                    
                }
                else{
                    alert('O campo escola é obrigatório.');
                    document.getElementById(tipo+'_escola').style.boxShadow = "0px 0px 12px #fe1313";
                }
            }
            else{
                alert('O campo nome é obrigatório.');
                document.getElementById(tipo+'_nome').style.boxShadow = "0px 0px 12px #fe1313";
            }
    }
       
}

function cadastro_usuario(tipo){
    if (tipo == 'aluno'){
        nome = document.getElementById(tipo+'_nome').value;
        nascimento = document.getElementById(tipo+'_nascimento').value;
        sexo = document.getElementById(tipo+'_sexo').value;
        escola = document.getElementById(tipo+'_escola').value;
        turma = document.getElementById(tipo+'_turma').value;
        if (nome != '' && nome != null){
//            if (nascimento != '' && nascimento != null){
                if (escola != '' && escola != null){
                    $("#loading").css('display','none')
                    $.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, nascimento:nascimento, sexo:sexo, vinculo_escola:escola, vinculo_turma:turma},function(data){
                        window.location.replace(data);
                    });
                    
                }
                else{
                    alert('O campo escola é obrigatório.');
                    document.getElementById(tipo+'_escola').style.boxShadow = "0px 0px 12px #fe1313";
                }
//            }
//            else{
//                alert('O campo nascimento é obrigatório.');
//                document.getElementById(tipo+'_nascimento').style.boxShadow = "0px 0px 12px #fe1313";
//            }
        }
        else{
            alert('O campo nome é obrigatório.');
            document.getElementById(tipo+'_nome').style.boxShadow = "0px 0px 12px #fe1313";
        }

    }
    else if(tipo == 'professor'){
        nome = document.getElementById(tipo+'_nome').value;
        nascimento = document.getElementById(tipo+'_nascimento').value;
        email = document.getElementById(tipo+'_email').value;
        escola = document.getElementById(tipo+'_escola').value;
        turma = document.getElementById(tipo+'_turma').value;

        if (nome != '' && nome != null){
//            if (nascimento != '' && nascimento != null){
                if (email != '' && email != null && emailValidador(tipo+'_email')){

                    if(!validar_se_email_existe(email)){
                        if (escola != '' && escola != null){
                            $("#loading").css('display','block');
                            $.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, nascimento:nascimento, email:email, vinculo_escola:escola, vinculo_turma:turma},function(data){
                                window.location.replace(data);
                            });
                            location.reload();
                        }
                        else{
                            alert('O campo escola é obrigatório.');
                            document.getElementById(tipo+'_escola').style.boxShadow = "0px 0px 12px #fe1313";
                        }

                    }
                    else{
                        alert('O email digitado já foi cadastrado no nosso sitema.');
                        document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
                    }
                }
                else{
                    alert('O campo email é obrigatório.');
                    document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
                }
//            }
//            else{
//                alert('O campo nascimento é obrigatório.');
//                document.getElementById(tipo+'_nascimento').style.boxShadow = "0px 0px 12px #fe1313";
//            }
        }
        else{
            alert('O campo nome é obrigatório.');
            document.getElementById(tipo+'_nome').style.boxShadow = "0px 0px 12px #fe1313";
        }
    }
    else if(tipo == 'diretor'){
        nome = document.getElementById(tipo+'_nome').value;
        nascimento = document.getElementById(tipo+'_nascimento').value;
        email = document.getElementById(tipo+'_email').value;
        escola = document.getElementById(tipo+'_escola').value;
        if (nome != '' && nome != null){
//            if (nascimento != '' && nascimento != null){
                if (email != '' && email != null && emailValidador(tipo+'_email')){
                    if(!validar_se_email_existe(email)){
                        if (escola != '' && escola != null){
                            $("#loading").css('display','block');
                            $.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, nascimento:nascimento, email:email, vinculo_escola:escola},function(data){
                                window.location.replace(data);
                            });
                            
                        }
                        else{
                            alert('O campo escola é obrigatório.');
                            document.getElementById(tipo+'_escola').style.boxShadow = "0px 0px 12px #fe1313";
                        }

                    }
                    else{
                        alert('O email digitado já foi cadastrado no nosso sitema.');
                        document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
                    }
                }
                else{
                    alert('O campo email é obrigatório.');
                    document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
                }
//            }
//            else{
//                alert('O campo nascimento é obrigatório.');
//                document.getElementById(tipo+'_nascimento').style.boxShadow = "0px 0px 12px #fe1313";
//            }
        }
        else{
            alert('O campo nome é obrigatório.');
            document.getElementById(tipo+'_nome').style.boxShadow = "0px 0px 12px #fe1313";
        }
    }
    else if(tipo == 'gestor'){
        nome = document.getElementById(tipo+'_nome').value;
        nascimento = document.getElementById(tipo+'_nascimento').value;
        email = document.getElementById(tipo+'_email').value;
        rede = document.getElementById(tipo+'_rede').value;

        if (nome != '' && nome != null){
                if (email != '' && email != null && emailValidador(tipo+'_email')){
                    if(!validar_se_email_existe(email)){
                        if (rede != '' && rede != null){
                            $("#loading").css('display','block');
                            $.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, nascimento:nascimento, email:email, vinculo_rede:rede},function(data){
                                window.location.replace(data);
                            });
                        }
                        else{
                            alert('O campo rede é obrigatório.');
                            document.getElementById(tipo+'_rede').style.boxShadow = "0px 0px 12px #fe1313";
                        }
                    }
                    else{
                       alert('O email digitado já foi cadastrado no nosso sitema.');
                        document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
                    }

                }
                else{
                    alert('O campo email é obrigatório.');
                    document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
                }

        }
        else{
            alert('O campo nome é obrigatório.');
            document.getElementById(tipo+'_nome').style.boxShadow = "0px 0px 12px #fe1313";
        }
    }
    else if(tipo == 'responsavel'){
        nome = document.getElementById(tipo+'_nome').value;
        email = document.getElementById(tipo+'_email').value;
        aluno = document.getElementById(tipo+'_aluno').value;

		if (nome != '' && nome != null){
			if (email != '' && email != null && emailValidador(tipo+'_email')){
			    if (aluno != '' && aluno != null){
				    if(!validar_se_email_existe(email)){
				        $("#loading").css('display','block');
					    $.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, email:email, vinculo_aluno:aluno},function(data){
						    window.location.replace(data);
					    });

				    }else{
				            alert('O email digitado já foi cadastrado no nosso sitema.');
                            document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
                            }
			    }else{
			        alert('O responsavel precisa estar associado a um aluno');
                    document.getElementById(tipo+'_aluno').style.boxShadow = "0px 0px 12px #fe1313";
			    }
		    }else{
                    alert('O campo email é obrigatorio');
                    document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";

			}
		}else{
			alert('O campo nome é obrigatório.');
            document.getElementById(tipo+'_nome').style.boxShadow = "0px 0px 12px #fe1313";
		}
    }
    else if(tipo == 'coordenador'){
        nome = document.getElementById(tipo+'_nome').value;
        nascimento = document.getElementById(tipo+'_nascimento').value;
        email = document.getElementById(tipo+'_email').value;
        escola = document.getElementById(tipo+'_escola').value;

        if (nome != '' && nome != null){
			if (email != '' && email != null && emailValidador(tipo+'_email')){
			    if(escola != '' && escola !=null){
				    if(!validar_se_email_existe(email)){
				        $("#loading").css('display','block');
					    $.post('/usuario/cadastro_usuario', {tipo:tipo, nome:nome, email:email, vinculo_aluno:aluno},function(data){
						    window.location.replace(data);
					            });
					}else{
                            alert('O email digitado já foi cadastrado no nosso sitema.');
                            document.getElementById(tipo+'_escola').style.boxShadow = "0px 0px 12px #fe1313";
                    }
				}else{
				        alert('O campo escola é obrigatório.');
                        document.getElementById(tipo+'_escola').style.boxShadow = "0px 0px 12px #fe1313";
				}
			}else{
                alert('O campo email é obrigatorio');
                document.getElementById(tipo+'_email').style.boxShadow = "0px 0px 12px #fe1313";
			}
		}else{
		    alert('O campo nome é obrigatorio');
            document.getElementById(tipo+'_nome').style.boxShadow = "0px 0px 12px #fe1313";
		}


    }
}



  function test(ide) {
   console.log(ide);
    y = document.getElementById(ide).innerHTML;
    x = document.getElementById("nova-escola").style.display;
    prof = document.getElementById("novo-prof").style.display;
    diretor = document.getElementById("novo-diretor");
    gestor = document.getElementById("novo-gestor");
    aluno = document.getElementById("novo-aluno");
    console.log(x, y)
    if (prof == "none") {
    document.getElementById("novo-prof").style.display = 'block';
    document.getElementById(ide).innerHTML = '<i id="setinha" class="fas fa-angle-up"></i>';
    }
    else {
    document.getElementById("nova-escola").style.display = 'none';
    document.getElementById(ide).innerHTML = '<i id="setinha" class="fas fa-angle-down"></i>';
    // document.getElementById(drop).style.display='block':
    }
    }

  function allow_edit(content_class_id){
    console.log('teste');

    console.log('teste');
    $('.disabled'+content_class_id).prop("disabled", false);
    $('#icone_edit'+content_class_id).hide();
    $('#edit'+content_class_id).show();
}

function update_aluno(id){
    console.log(id);
    id = document.getElementById('id_aluno'+id).value;
    nome = document.getElementById('nome'+id).value;
    login = document.getElementById('aluno_login'+id).value;

      try { // statements to try
    turma = document.getElementById('aluno_turma'+id).value;
    console.log('id ,nome ,login ',id,nome,login,turma);


    if (turma != '' && turma !=null){
        if (nome != '' && nome != null){
            if(login != '' && login != null){
                    console.log('eits',nome,id);
                    $.post('/aluno/update_aluno', {id:id, nome:nome,login:login,turma:turma},function(data){
                        console.log("hm");
                    });
                location.reload();
                }
                else{
            alert('o campo login nao pode estar vazio ');
            }
        }else{
            alert('O campo nome é obrigatório.');
            document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
            }
        }

}
       catch (e) {
  console.log('erro',e);
   if (nome != '' && nome != null){
            if(login != '' && login != null){
                    console.log('dados aluno',nome,login);
                    $.post('/aluno/update_aluno', {id:id, nome:nome,login:login},function(data){
                        console.log("hm");
                    });
                location.reload();
                }
                else{
            alert('o campo login nao pode estar vazio ');
            }
        }else{
            alert('O campo nome é obrigatório.');
            document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
            }
}
    }


function update_observador(id){
    console.log('entrei?');
    id = document.getElementById("observador_id"+id).value;
    nome = document.getElementById("nome_obs"+id).value;
    email= document.getElementById("email"+id).value;
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    teste = email.match(mailformat);
    console.log(teste,email);
    if (nome != '' && nome != null){
            if (email != '' && nome !=null && email.match(mailformat)){
                if(validar_se_email_existe(email)==false){
                console.log('email existe');
                $.post('/observador/update_observador', {id:id, nome:nome,email:email},function(data){
                    console.log("hm");
                });
                location.reload();
                }
                else{
                console.log("hm,emailnao existe");
                $.post('/observador/update_observador', {id:id, nome:nome},function(data){
                });
//                location.reload();
                }
               }else{
            alert('Por favor , digite um email valido');
            }

    }else{
        alert('O campo nome é obrigatório.');
        document.getElementById("nome").style.boxShadow = "0px 0px 12px #fe1313";
        }
        }

function allow_edit_obs(content_class_id){
    console.log('teste');

    console.log('teste');
    $('.disabledo'+content_class_id).prop("disabled", false);
    $('#icone_edito'+content_class_id).hide();
    $('#edito'+content_class_id).show();

}
//function readURL(input) {
//            if (input.files && input.files[0]) {
//                var reader = new FileReader();
//                ext=input.files[0].name.split('.')[1];
//                console.log(ext,input.files[0].size,input.files);
//
//                if (ext != 'png' && ext!= 'jpg' && ext!= 'jpeg'){
//                       $('#error').css('display','block');
//
//                }else if(input.files[0].size > 1048576){
//                alert('por favor selecione uma imagem de tamanho 1MB ou menor');
//
//                 }
//                 reader.onload = function (e) {
//                 console.log('que',e);
//                    $('.blah').attr('src', e.target.result)
//                        //.width(150)
//                        //.height(200);
//                 };
//                 reader.readAsDataURL(input.files[0]);
//                 $('#salv').css('display','block');
//
//
//
//
//            }
//        }
//
//    interact('.draggable').draggable({
//    // enable inertial throwing
//    inertia: false,
//    // keep the element within the area of it's parent
//    restrict: {
//      restriction: "parent",
//      endOnly: false,
//      elementRect: { top: 0, left: 0, bottom: 1.1, right: 1.1 }
//    },
//
//    // call this function on every dragmove event
//    onmove: dragMoveListener,
//    // call this function on every dragend event
//    onend: function (event) {
//    }
//  });
//
//  function dragMoveListener (event) {
//    console.log('test',event.target);
//    var target = event.target,
//
//        // keep the dragged position in the data-x/data-y attributes
//        x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
//        y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;
//    // translate the element
//    target.style.webkitTransform =
//    target.style.transform =
//      'translate(' + x + 'px, ' + y + 'px)';
//
//
//
//    // update the posiion attributes
//    target.setAttribute('data-x', x);
//    target.setAttribute('data-y', y);
//    var z; // x negativo
//    var w;  //y negativo
//    console.log('hm',x,y);
//    $.ajax({
//     url: '/salvar_css_foto',
//     data: {
//        posicao_foto:'transform:translate(' + x + 'px, ' + y + 'px)'
//    },
//    dataType: 'json',
//    type: 'post'
//});
//  }
//}
//
//    id = document.getElementById('id_turma'+id).value;
//    nome = document.getElementById('nome'+id).value;
//    login = document.getElementById();
//    console.log('testando',id,nome,login);
//
//
//}

//function nao-sair-sem-salvar(id){
//
//alert('Voce nao salvou a sua ediçao , tem certeza que deseja sair ?');
//
//
//}