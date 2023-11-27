#!/usr/bin/node
// Prints the factorial where  of the first argument.
const factorial = (n) => {
  if (isNaN(n) || n <= 0) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(process.argv[2])));
