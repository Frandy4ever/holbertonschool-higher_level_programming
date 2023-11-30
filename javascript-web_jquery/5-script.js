// Add <li> </li> element to list when user clicks on DIV#add_item
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
