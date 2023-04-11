#!/usr/bin/node

const { argv } = require('process');
let len1 = 0;

argv.forEach(() => len1++);

console.log(len1 === 2 ? 'No argument' : argv[2]);
