#!/usr/bin/node

const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(api, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
