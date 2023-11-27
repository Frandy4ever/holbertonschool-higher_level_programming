#!/usr/bin/node
// Prints value of the first argument passed.
const cmdArgs = process.argv[2];

console.log((cmdArgs) ? cmdArgs : 'No argument');
