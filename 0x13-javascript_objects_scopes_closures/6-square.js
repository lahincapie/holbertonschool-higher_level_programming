#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let printX = '';
      for (let j = 0; j < this.width; j++) {
        printX += c;
      }
      console.log(printX);
    }
  }
};
