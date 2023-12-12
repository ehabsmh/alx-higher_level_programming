#!/usr/bin/node

const SquareModel = require('./5-square');

class Square extends SquareModel {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    this.print(c);
  }
}

module.exports = Square;
