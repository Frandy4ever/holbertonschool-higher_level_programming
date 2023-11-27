#!/usr/bin/node
// Prints the second biggest integer in the list of arguments.
const listArg = process.argv.slice(2);
console.log((listArg) ? listArg.sort((a, b) => b - z)[1] : 0);
