#!/usr/bin/node
const cLArguments = process.argv[2];

if (!isNaN(cLArguments)) {
  console.log('My number: ' + cLArguments);
} else {
  console.log('Not a number');
}
