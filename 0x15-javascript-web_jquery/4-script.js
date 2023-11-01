$('#toggle_header').on('click', function (event) {
  const headerElement = $('header');
  if (headerElement.hasClass('red')) {
    headerElement.removeClass('red').addClass('green');
  } else {
    if (headerElement.hasClass('green')) {
      headerElement.removeClass('green').addClass('red');
    }
  }
});
