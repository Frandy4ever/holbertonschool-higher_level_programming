#!/usr/bin/node
// Prints msg depending on number of arguments passed.
const cmdArgs = process.argv[2];
if (cmdArgs < cmdArgs[2]) console.log('No argument');
else if (cmdArgs) console.log('Argument found');
else console.log('Arguments found');
