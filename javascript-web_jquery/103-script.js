// Fetches ahd prints how to say “Hello” depending of the language
$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val().trim();

    if (languageCode === '') {
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
  }

  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  $('#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
