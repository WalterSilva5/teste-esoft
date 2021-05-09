$(document).ready(function () {
    $("input[name='cep2']").on("change keyup", function () {
      cep = $("input[name='cep2']").val();
      let url = `https://viacep.com.br/ws/${cep}/json/`;
      console.log(url);
      $.ajax({
        type: "POST",
        crossDomain: true,
        dataType: "jsonp",
        url: url,
        success: function (jsondata) {
          $.each(jsondata, function (key, item) {
            $(`input[name='${key}']`).val(item);
            if (key == "logradouro") {
              item_splited = item.split(" ");
  
              numero = item_splited[item_splited.length - 1];
              console.log(item_splited);
              //verifica se o logradouro tem numero e aplica a input do numero
              if (numero == parseInt(numero)) {
                $(`input[name='numero']`).val(numero);
                novo_logradouro = "";
                for (palavra = 0; palavra < item_splited.length - 1; palavra++) {
                  novo_logradouro = novo_logradouro + " " + item_splited[palavra];
                }
                console.log(novo_logradouro);
                $(`input[name='logradouro']`).val(novo_logradouro);
              }
            }
          });
        },
      });
    });
  });
  