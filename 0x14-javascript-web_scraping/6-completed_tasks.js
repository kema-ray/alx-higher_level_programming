#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (error, result, body) => {
    const completed = {};

    if (error) {
      console.log(error);
    }
    JSON.parse(body).forEach(element => {
      if (element.todo) {
        if (!completed[element.userId]) {
          completed[element.userId] = 0;
        }
        completed[element.userId]++;
      }
    });
    console.log(completed);
  });
}
