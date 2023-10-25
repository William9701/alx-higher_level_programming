#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18; // Wedge Antilles' character ID

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    const films = JSON.parse(body);
    const filmsWithWedgeAntilles = films.filter((film) => film.characters.includes(characterId));
    console.log(`Number of films where Wedge Antilles is present: ${filmsWithWedgeAntilles.length}`);
  }
});
