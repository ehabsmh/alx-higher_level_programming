#!/usr/bin/node

const process = require('process');
const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2, 4);

let url = '';
let filePath = '';

if (args.length === 2) {
  [url, filePath] = [args[0], args[1]];
} else {
  console.log('Usage: ./5-request_store.js URL File_Path');
  process.exit(1);
}

request.get(url, (err, _, body) => {
  try {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) throw err;
    });

    if (err) throw err;
  } catch {
    console.log(err);
  }
});
