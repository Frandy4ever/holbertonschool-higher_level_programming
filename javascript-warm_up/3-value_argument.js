#!/usr/bin/node
const arguments = process.argv
if (arguments < 3) {
  console.log('No arguments');
}else {
  console.log(arguments[2]);
}
