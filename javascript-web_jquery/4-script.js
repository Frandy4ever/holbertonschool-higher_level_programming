// Toggle the class of from green to red when the user clicks on the tag DIV#toggle_header
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
