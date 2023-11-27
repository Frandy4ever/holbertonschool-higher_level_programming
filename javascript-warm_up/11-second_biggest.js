#!/usr/bin/node
// Prints the second biggest integer in the list of arguments.
const listArgs = arg.slice(2);
console.log((listArgs) ? listArgs.sort((a, b) => b - a)[listArgs.length - 2] : 0);
