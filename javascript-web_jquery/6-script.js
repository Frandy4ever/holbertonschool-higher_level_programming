// Update test of header tag when user clicks on tag DIV#update_header
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
