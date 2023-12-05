#!/usr/bin/node
// Print a Star Wars movie title where the episode number matches a given integer.
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) { console.log(error); } else {
    console.log(JSON.parse(body).title);
  }
});
