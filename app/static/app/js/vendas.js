function imprimir_cupom() {
    var conteudo = $("#cupom").html();
    var win = window.open();
    win.document.write(conteudo);
    win.print();
    //win.close();
}