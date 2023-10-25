#!/usr/bin/node
const fs = require('fs');

// Check if the user provided a file path as a command-line argument
if (process.argv.length < 3) {
  console.log('Usage: node read-file.js <file-path>');
  process.exit(1); // Exit with an error code
}

// Get the file path from the command-line argument
const filePath = process.argv[2];
const write = process.argv[3];

fs.writeFile(filePath, write, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
