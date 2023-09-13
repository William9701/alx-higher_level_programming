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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
