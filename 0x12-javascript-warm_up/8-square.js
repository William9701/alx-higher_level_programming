#!/usr/bin/node

const count = process.argv[2];
const dcount = parseInt(count);
if (isNaN(dcount)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < dcount) {
    console.log('X'.repeat(dcount));
    i++;
  }
}
