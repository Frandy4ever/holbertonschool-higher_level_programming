// Update HTML element text color when another HTML element is clicked using JQuery API
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
