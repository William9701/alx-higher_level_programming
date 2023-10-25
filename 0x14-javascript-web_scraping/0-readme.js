#!/usr/bin/node
const fs = require('fs');

// Check if the user provided a file path as a command-line argument
if (process.argv.length < 3) {
  console.log('Usage: node read-file.js <file-path>');
  process.exit(1); // Exit with an error code
}

// Get the file path from the command-line argument
const filePath = process.argv[2];

// Read and print the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurred, print the error object
    console.error(err);
  } else {
    // Print the file content
    console.log(data);
  }
});
