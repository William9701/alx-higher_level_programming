#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c) {
    const box = c || 'X';
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += box;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
