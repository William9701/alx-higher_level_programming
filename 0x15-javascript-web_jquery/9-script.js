$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=en',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    // Display the translation of "hello" in the DIV#hello
    $('#hello').text(data.hello);
  },
  error: function (xhr, status, error) {
    // Handle any errors that occur during the request
    $('#hello').text('Translation: Error - ' + error);
  }
});
