#!/usr/bin/node

const process = require('process');
const request = require('request');

let movieID = process.argv.slice(2, 3);

if (movieID.length) {
  movieID = movieID.toString();
} else {
  console.log('Usage: ./0-readme.js movieID');
  process.exit(1);
}

const endpoint = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(endpoint, { json: true }, (err, res, body) => {
  try {
    console.log(body.title);
    if (err) throw err;
  } catch {
    console.log(err);
  }
});
