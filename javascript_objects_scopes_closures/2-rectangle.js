#!/usr/bin/node
// Create attribute width and height if class is not empty

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
