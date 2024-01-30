#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const args = process.argv.slice(2, 4);

let filePath = '';
let myText = '';

if (args.length === 2) {
  [filePath, myText] = [args[0], args[1]];
} else {
  console.log('Usage: ./0-readme.js filePath');
}

fs.writeFile(filePath, myText, { encoding: 'utf-8' }, (err) => {
  if (err) console.log(err);
});
