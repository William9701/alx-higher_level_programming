#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length <= 3) {
  console.log('Please provide the API URL and the file path as arguments');
  process.exit(-1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (!error) {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.log(error); // Print the error if one occurred
  }
});
