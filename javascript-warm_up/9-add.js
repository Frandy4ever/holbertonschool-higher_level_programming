#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  console.log(a + b);
}

add(process.argv[2], process.argv[3]);
