#!/usr/bin/node
// Rectangle class with constructor having two arguments w and h

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
