#!/usr/bin/node

// Script prints a square

let i = 0;
const y = 'X';
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  while (i < x) {
    console.log(y.repeat(x));
    i++;
  }
}
