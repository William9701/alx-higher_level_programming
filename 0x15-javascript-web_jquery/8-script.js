$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    const movies = data.results; // Get an array of movies

    // Iterate through the array and add movie titles to the UL#list_movies
    for (let i = 0; i < movies.length; i++) {
      const movieTitle = movies[i].title;
      $('#list_movies').append('<li>' + movieTitle + '</li>');
    }
  },
  error: function (xhr, status, error) {
    // Handle any errors that occur during the request
    $('#list_movies').append('<li>Error: ' + error + '</li>');
  }
});
