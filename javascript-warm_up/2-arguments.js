#!/usr/bin/node
// Prints msg depending on number of arguments passed.
const cmdArgs = process.argv.length;
if (cmdArgs <= 2) console.log('No argument');
else if (cmdArgs == 3) console.log('Argument found');
else console.log('Arguments found');
