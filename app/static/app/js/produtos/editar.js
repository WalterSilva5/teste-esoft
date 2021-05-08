//busca os dados do produto que vai ser editado
$("button[name='botao_editar_produto']").click(function () {
  id = $(this).attr("id");
  $.ajax({
    type: "post",
    url: "http://localhost:8000/produtos/dados_do_produto",
    data: {
      id: id,
    },
    success: function (result) {
      //console.log(result)
      let dados = result.produto[0];
      $("#id_edit").val(dados.id);
      $("#nome_edit").val(dados.nome);
      $("#preco_edit").val(
        parseFloat(dados.preco).toLocaleString("pt-br", {
          minimumFractionDigits: 2,
        })
      );
      $("#estoque_edit").val(
        parseFloat(
          dados.estoque.toLocaleString("pt-br", { minimumFractionDigits: 2 })
        )
      );
    },
    error: function (result) {
      console.log(result);
    },
  });
});

//salva a edição do produto
$("button[name='botao_salvar_editar_produto']").click(function () {
  id = $(this).attr("id");

  $.ajax({
    type: "post",
    url: "http://localhost:8000/produtos/atualizar_produto",
    data: {
      id: $("#id_edit").val(),
      nome: $("#nome_edit").val(),
      preco: parseFloat($("#preco_edit").val()),
      estoque: parseFloat($("#estoque_edit").val()),
    },
    success: function (result) {
      console.log(result);
      if (result == "OK") {
        sucesso();
      } else if (result == "NOME_JA_CADASTRADO") {
        erro("NOME JA ESTA CADASTRADO");
      } else if (result == "ERRO_DESCONHECIDO") {
        erro(result);
      } else if (result == "ESTOQUE_NEGATIVO") {
        erro("ESTOQUE NÃO PODE SER NEGATIVO!");
      } else if (result == "PRECO_NEGATIVO") {
        erro("PREÇO NÃO PODE SER NEGATIVO!");
      } else {
        erro("ERRO_DESCONHECIDO");
      }
    },
    error: function (result) {
      if (result.responseText.split(" ")[0] == "ValueError") {
        mensagem =
          "VERIFIQUE AS INFORMAÇÕES! - " + result.responseText.split(" ")[0];
      } else {
        mensagem = result.responseText.split(" ")[0];
      }
      console.log(result);
      erro("ERRO: " + mensagem);
    },
  });
});
function sucesso() {
  $("#edit_produto_cadastro_efetuado").removeClass("d-none");
  $("#edit_produto_cadastro_nao_efetuado").addClass("d-none");
  $("input").val("");
}
function erro(mensagem) {
  //$("#edit_produto_cadastro_efetuado").addClass("d-none");
  $("#edit_produto_cadastro_nao_efetuado").removeClass("d-none");
  $("#edit_mensagem_erro").text(mensagem);
}
$("#modal_editar_produto").on("hidden.bs.modal", function () {
  $("#edit_produto_cadastro_nao_efetuado").addClass("d-none");
  $("#edit_produto_cadastro_nao_efetuado").addClass("d-none");
  $("#form_editar_produto").trigger("reset");
  location.reload();
});
