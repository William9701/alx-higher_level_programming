#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.log('Please provide the API URL as an argument');
  process.exit(-1);
}

const url = process.argv[2];
let count = 0;
let movie = '';
request(url, function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body);
    for (movie of movies.results) {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count += 1;
      }
    }
    console.log(count);
  } else {
    console.error(error); // Print the error if one occurred
  }
});
