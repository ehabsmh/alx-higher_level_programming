#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(firstArg) || n < 2) return 1;

  return n * factorial(n - 1);
}

console.log(factorial(firstArg));
