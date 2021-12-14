#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let charX = '';
      for (let j = 0; j < this.width; j++) {
        charX += 'X';
      }
      console.log(charX);
    }
  }

  rotate () {
    const exchanges = this.width;
    this.width = this.height;
    this.height = exchanges;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
