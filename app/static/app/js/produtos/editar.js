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
      let dados = result.produto[0];
      console.log(dados);
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
    },
    error: function (result) {
      console.log(result);
    },
  });
});
