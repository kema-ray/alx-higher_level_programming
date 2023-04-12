#!/usr/bin/node

const { argv } = require('process');
const args = argv.slice(2);
let result = 0;
let finalResult = [];

if (args.length > 1) {
  finalResult = [...new Set(args.map((e) => parseInt(e)).sort((a, b) => b - a))];
  result = finalResult.length > 1 ? finalResult[1] : finalResult[0];
}

console.log(result);
