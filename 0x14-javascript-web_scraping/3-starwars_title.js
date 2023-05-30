#!/usr/bin/node

const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request.get(api + id, function (error, result, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
