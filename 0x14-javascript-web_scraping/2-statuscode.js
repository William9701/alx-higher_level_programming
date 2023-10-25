#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.log('Please provide a URL as an argument');
  process.exit(-1);
}

const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    console.log('code:', response && response.statusCode); // Print the status code
  } else {
    console.log(error); // Print the error if one occurred
  }
});
