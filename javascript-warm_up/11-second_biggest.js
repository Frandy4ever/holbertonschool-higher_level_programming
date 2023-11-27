#!/usr/bin/node
// Prints the second biggest integer in the list of arguments.
const listArgs = arg.slice(2);
console.log((listArgs.length < 2) ? 0 : listArgs.sort((a, b) => b - a)[1]);
