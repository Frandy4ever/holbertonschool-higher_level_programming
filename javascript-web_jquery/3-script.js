// Using jQuery API to add class red to <header> when DIV#red_header is clicked
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('header').addClass('red');
  });
});
