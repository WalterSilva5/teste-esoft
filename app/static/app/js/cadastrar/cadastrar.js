//verifica se todas as inputs estão prenchidas
function verificar_preenchimento(){
  var elements = $("input");
  //console.log(elements);
  for (var i = 0; i < elements.length; i++) {
    try{
      v = elements["i"].value;  
    }catch(e){
      erro("PREENCHA TODOS OS CAMPOS!")
    }
  }
}

//verifica se as senhas sao iguais
$(`input[name='repetir_senha']`).on("change keyup", function () {
  if (
    $(`input[name='repetir_senha']`).val() != $(`input[name='senha']`).val()
  ) {
    $("#senhas_diferentes").removeClass("d-none");
    $('input[name="btn_submit"]').addClass("d-none");
  } else {
    $("#senhas_diferentes").addClass("d-none");
    $('input[name="btn_submit"]').removeClass("d-none");
  }
});
//verifica se ja esta cadastrado
$("input[name='email']").on("change keyup", function () {
  email = $("input[name='email']").val();
  console.log(email);

  $.ajax({
    type: "post",
    url: "http://localhost:8000/cadastrar/verifica_usuario_cadastrado",
    data: {
      email: email,
    },
    success: function (result) {
      if (result == "CADASTRADO") {
        erro("ERRO! ESTE EMAIL JA ESTA CADASTRADO!");
      }
    },
  });

  function erro(mensagem) {
    $("#mensagem_erro_cadastro").text(mensagem);
    $("#cadastro_efetuado").addClass("d-none");
    $("#erro_cadastro").removeClass("d-none");
  }
  function sucesso() {
    $("#cadastro_efetuado").removeClass("d-none");
    $("#erro_cadastro").addClass("d-none");
  }
});
function cadastrar_usuario() {
  nome = $(`input[name='nome']`).val();
  email = $(`input[name='email']`).val();
  senha = $(`input[name='senha']`).val();
  cep2 = $(`input[name='cep2']`).val();
  logradouro = $(`input[name='logradouro']`).val();
  localidade = $(`input[name='localidade']`).val();
  numero = $(`input[name='numero']`).val();
  bairro = $(`input[name='bairro']`).val();
  cidade = $(`input[name='cidade']`).val();
  uf = $(`input[name='uf']`).val();
  verificar_preenchimento()
  
  $.ajax({
    type: "post",
    url: "http://localhost:8000/cadastrar/efetuar_cadastro",
    data: {
      nome: nome,
      email: email,
      senha: senha,
      cep2: cep2,
      logradouro: logradouro,
      numero: numero,
      bairro: bairro,
      localidade: localidade,
      uf: uf,
    },
    success: function (result) {
      console.log(result);
      if(result=="CADASTRADO"){
        erro("USUARIO JA ESTA CADASTRADO!")
      }else if(result == "OK"){
        sucesso();
      }
     },
    error: function (result) {
      mesg = result.responseText.split(" ")[0];
      if ( msg == "ValueError") {
        mensagem =
          "VERIFIQUE AS INFORMAÇÕES! - " + result.responseText.split(" ")[0];
      } else if (msg=="IntegrityError"){
        erro("PREENCHA TODOS OS CAMPOS!");
      }else {
        erro("ERRO: " + mensagem);
      }
      console.log(result);
    },
  });

  function sucesso() {
    $("#cadastro_efetuado").removeClass("d-none");
    //window.location.replace("/cadastrar");
    //alert("CADASTRO EFETUADO COM SUCESSO!")
    $("#form_cadastrar_usuario").trigger("reset");
    $("#erro_cadastro").addClass("d-none");

  }
  function erro(mensagem) {
    $("#erro_cadastro").text(mensagem);
    $("#cadastro_efetuado").removeClass("d-none");
    $("#cadastro_efetuado").addClass("d-none");
  }
}

function sucesso() {
  $("#cadastro_efetuado").removeClass("d-none");
  $("#erro_cadastro").addClass("d-none");
  alert("CADASTRO EFETUADO COM SUCESSO!");
  $("#form_cadastrar_usuario").trigger("reset");

}
function erro(mensagem) {
  $("#mensagem_erro_cadastro").text(mensagem);
  $("#cadastro_efetuado").addClass("d-none");
  $("#erro_cadastro").removeClass("d-none");
}


