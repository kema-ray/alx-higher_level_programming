#!/usr/bin/node

const { argv } = require('process');
const number = parseInt(argv[2]);
const printC = (x) => {
  for (; x > 0; x--) console.log('C is fun');
};

Number.isInteger(number) ? printC(number) : console.log('Missing number of occurrences');
