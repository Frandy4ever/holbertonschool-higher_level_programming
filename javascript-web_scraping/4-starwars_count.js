#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (err, response, body) {
  if (err) { console.error(err); }
  const results = JSON.parse(body).results;
  for (const film of results) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
