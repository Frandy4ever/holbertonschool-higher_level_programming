#!/usr/bin/node
// Rectangle class with constructor having two arguments w and h
module.exports = class Rectangle {  
  constructor(w, h) {
    this.width = (w  > 0) ? w : 0;
    this.height = (h > 0) ? h : 0;
  }
};
