// Fetches and prints how to say “Hello” depending of the language
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

    if (languageCode.trim() === '') {
      alert('Please enter a language code.');
      return;
    }

    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`,
      method: 'GET',
      dataType: 'json',
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function () {
        console.log('Error fetching translation.');
      }
    });
  });
});
