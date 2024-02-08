const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data, textStatus) {
    if (textStatus == 'success') $('DIV#hello').text(data.hello);
  });
});
