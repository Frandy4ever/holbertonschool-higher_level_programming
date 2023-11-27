#!/usr/bin/node
// Print x times “C is fun” while x is the first argument of the script
const x = parseInt(process.argv[2]);
if (x) for (let i = 0; i <= x; i++) console.log('C is fun');
