$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

    // Make an AJAX request to fetch the translation
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode,
      method: 'GET',
      dataType: 'json',
      success: function (data) {
        const translation = data.hello;
        $('#hello').text('Translation: ' + translation);
      },
      error: function (xhr, status, error) {
        $('#hello').text('Translation: Error - ' + error);
      }
    });
  });
});
