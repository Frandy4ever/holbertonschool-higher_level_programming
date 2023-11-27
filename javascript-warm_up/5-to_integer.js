#!/usr/bin/node
// Prints first argument if it can be converted to an integer
const intArgs = parseInt(process.argv.slice(2));
console.log(intArgs ? `My number: ${intArgs}` : 'Not a number');
