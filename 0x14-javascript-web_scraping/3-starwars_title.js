#!/usr/bin/node
const request = require('request');

if (process.argv.length <= 2) {
  console.log('Please provide a movie ID as an argument');
  process.exit(-1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error) {
    const movie = JSON.parse(body);
    console.log(movie.title); // Print the movie title
  } else {
    console.log(error); // Print the error if one occurred
  }
});
