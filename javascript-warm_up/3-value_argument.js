#!/usr/bin/node
const firstArgument = process.argv[2];
if (firstArgument) {
  console.log(firstArgument);
} else {
  console.log('No argument');
}
