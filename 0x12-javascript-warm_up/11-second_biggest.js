#!/usr/bin/node

// Script prints second biggest integer

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argsList = process.argv.slice(2);
  const num = argsList.map(Number);
  const sortedNumbers = num.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
