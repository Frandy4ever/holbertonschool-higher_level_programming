#!/usr/bin/node
// Using const for variable declaration (not allowed to use var)
const numArguments = process.argv.length - 2;

// Printing the message based on the number of arguments
if (numArguments === 0) {
  console.log('No argument');
} else if (numArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
