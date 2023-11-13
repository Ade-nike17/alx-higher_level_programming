#!/usr/bin/node

// Prints message based on number of args passed

if (process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument found');
}
