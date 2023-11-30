// Fetches and lists the title for all movies by using
// this URL: https://swapi-api.hbtn.io/api/films/?format=json
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      for (let i = 0; i < data.results.length; i++) {
        $('#list_movies').append('<li>' + data.results[i].title + '</li>');
      }
    },
    error: function () {
      console.log('Error fetching data.');
    }
  });
});
