#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return this.Rectangle;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // Loop through the rows (height)
    for (let i = 0; i < this.height; i++) {
      let row = '';
      // Loop through the columns (width)
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      // Print the row
      console.log(row);
    }
  }
}
module.exports = Rectangle;
