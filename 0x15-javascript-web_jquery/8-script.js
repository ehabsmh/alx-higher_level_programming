const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function (data, textStatus) {
  if (textStatus === 'success') {
    const movies = data.results;
    $.each(movies, function (_, movie) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
