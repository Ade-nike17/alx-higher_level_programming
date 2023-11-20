#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Object.create(Rectangle);
    } else if (w && h) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const y = 'X';
    let i = 0;
    while (i < this.height) {
      console.log(y.repeat(this.width));
      i++;
    }
  }
};
