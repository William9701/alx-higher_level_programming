$('#add_item').click(function () {
  // Create a new <li> element with the text "Item"
  const newItem = $('<li>Item</li>');

  // Add the new <li> element to the UL.my_list
  $('ul.my_list').append(newItem);
});
