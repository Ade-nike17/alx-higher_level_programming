#!/usr/bin/node

// Script prints numbers conerted to integers

const num = parseInt(process.argv[2]);

if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
