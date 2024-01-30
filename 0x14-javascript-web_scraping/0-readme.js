#!/usr/bin/node

const process = require('process');
const fs = require('fs');

let filePath = process.argv.slice(2, 3);

if (filePath.length) {
  filePath = filePath.toString();
} else {
  console.log('Usage: ./0-readme.js filePath');
}

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
  try {
    console.log(data);
    if (err) throw err;
  } catch {
    console.log(err);
  }
});
