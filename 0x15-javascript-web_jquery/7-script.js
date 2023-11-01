$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    // Extract the character name from the response data
    const characterName = data.name;

    // Display the character name in the DIV#character
    $('#character').text(characterName);
  },
  error: function (xhr, status, error) {
    // Handle any errors that occur during the request
    $('#character').text('Error: ' + error);
  }
});
