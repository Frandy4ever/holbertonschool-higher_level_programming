// Fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays 
// the value of hello from that fetch in the HTML’s tag DIV#hello.
$(document).ready(function () {
    $.ajax({
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        method: 'GET',
        dataType: 'json',
        success: function (data) {
        $('#hello').text(data.hello);
        },
        error: function () {
        console.log('Error fetching data.');
        }
    });
});