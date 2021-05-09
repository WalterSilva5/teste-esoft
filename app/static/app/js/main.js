data = new Date();
$("#ano").text(data.getFullYear());
$(document).ready(function () {
  $(document).on("focus", ":input", function () {
    $(this).attr("autocomplete", "off");
  });
});