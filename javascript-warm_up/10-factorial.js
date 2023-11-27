#!/usr/bin/node
// Prints the factorial where  of the first argument.
function factorial (n) {
  return (isNaN(n) || n <= 0) ? 1 : n * factorial(n - 1);
}
console.log(factorial(parseInt(process.argv[2])));
