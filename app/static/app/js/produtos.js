function cadastrar_produto() {
  $.ajax({
    type: "post",
    url: "http://localhost:8000/produtos/cadastrar_produto",
    data: {
      nome: $(`input[name='nome']`).val(),
      estoque: $(`input[name='estoque']`).val(),
      preco: $(`input[name='preco']`).val(),
    },
    success: function (result) {
      $('#produto_cadastro_efetuado').removeClass("d-none");
      $('#produto_cadastro_nao_efetuado').addClass("d-none");

      $('input').val("");
    },
    error: function(result){
      $('#produto_cadastro_efetuado').addClass("d-none");
      $('#produto_cadastro_nao_efetuado').removeClass("d-none");
    }
  });
}

$("#fechar_cadastro_de_produto").on('click', function(){
  $('input').val("");
});