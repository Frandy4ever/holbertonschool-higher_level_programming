#!/usr/bin/node
// Print the addition of first and second arguments using add(a, b) prototype.
const add = (a, b) => a + b;
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])))
