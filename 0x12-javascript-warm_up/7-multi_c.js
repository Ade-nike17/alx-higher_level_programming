#!/usr/bin/node

// Script prints x times "C is fun"

let i = 0;
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log("Missing number of occurrences");
} else {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
