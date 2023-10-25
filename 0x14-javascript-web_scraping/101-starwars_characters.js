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
    const characters = movie.characters;

    const characterPromises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (!error) {
            const character = JSON.parse(body);
            resolve(character.name);
          } else {
            reject(error);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((names) => names.forEach((name) => console.log(name)))
      .catch((error) => console.log(error));
  } else {
    console.log(error); // Print the error if one occurred
  }
});
