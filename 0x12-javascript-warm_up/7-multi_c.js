#!/usr/bin/node

const count = process.argv[2];
const dcount = parseInt(count);
if (isNaN(dcount)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < dcount; i++) {
    console.log('C is fun');
  }
}
