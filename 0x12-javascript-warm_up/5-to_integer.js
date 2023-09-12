#!/usr/bin/node

const arg = process.argv[2];
const value = parseInt(arg);

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + value);
}
