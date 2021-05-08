function cadastrar_produto() {
  let nome = $(`input[name='nome']`).val();
  let estoque = $(`input[name='estoque']`).val();
  let preco = $(`input[name='preco']`).val();
  $.ajax({
    type: "post",
    url: "http://localhost:8000/produtos/cadastrar_produto",
    data: {
      nome: nome,
      estoque: estoque,
      preco: preco,
    },
    success: function (result) {
      console.log(result);
      if (result == "OK") {
        sucesso();
      } else if (result == "PRODUTO_JA_CADASTRADO") {
        mensagem = "PRODUTO JA ESTA CADASTRADO";
      } else if (result == "ERRO_DESCONHECIDO") {
        mensagem = result;
      }else if(result == "ESTOQUE_NEGATIVO"){
        mensagem = "ESTOQUE NÃO PODE SER NEGATIVO!"
      }else if(result == "PRECO_NEGATIVO"){
        mensagem = "PREÇO NÃO PODE SER NEGATIVO!"
      }else {
        erro("ERRO_DESCONHECIDO");
      }
      erro(mensagem);
    },
    error: function (result) {
      erro("ERRO: "+mensagem);
    },
  });
}
function sucesso() {
  $("#produto_cadastro_efetuado").removeClass("d-none");
  $("#produto_cadastro_nao_efetuado").addClass("d-none");
  $("input").val("");
}
function erro(mensagem) {
  $("#produto_cadastro_efetuado").addClass("d-none");
  $("#produto_cadastro_nao_efetuado").removeClass("d-none");
  $("#mensagem_erro").text(mensagem);
}
$("#modal_adicionar_produto").on("hidden.bs.modal", function () {
  $("#produto_cadastro_nao_efetuado").removeClass("d-none");
  $("#produto_cadastro_nao_efetuado").addClass("d-none");
  $("#form_adicionar_produto").trigger("reset");
  location.reload();
});
