#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  request(`${process.argv[2]}`, (error, result, body) => {
    if (error) {
      console.log(error);
    } else if (body) {
      const films = JSON.parse(body).results.filter(
        x => x.characters.find(y => y.match(/\/people\/18\/?$/))
      );

      console.log(films.length);
    }
  });
}
