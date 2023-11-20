#!/usr/bin/node

// Script computes and prints factorial

function getFactorial (n) {
  if (isNaN(n) === true || n === 0) {
    return 1;
  } else {
    return (n * getFactorial(n - 1));
  }
}
console.log(getFactorial(parseInt(process.argv[2])));
