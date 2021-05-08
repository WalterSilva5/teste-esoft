$("button[name='botao_excluir_produto']").click(function () {
    id = $(this).attr("id")
    $.ajax({
      type: "post",
      url: "http://localhost:8000/produtos/excluir_produto",
      data: {
        id: id,
      },
      success: function (result) {
        alert(`PRODUTO ID: ${id} FOI EXCLUIDO!`);
        location.reload();
       }
    });
  });