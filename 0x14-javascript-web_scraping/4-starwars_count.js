#!/usr/bin/node

const process = require('process');
const request = require('request');

let apiUrl = process.argv.slice(2, 3);

if (apiUrl.length) {
  apiUrl = apiUrl.toString();
} else {
  console.log('Usage: ./4-starwars_count.js API_URL');
  process.exit(1);
}

request.get(apiUrl, { json: true }, (err, res, body) => {
  try {
    const movies = body.results;
    let count = 0;

    movies.forEach(movie => {
      movie.characters.forEach(char =>
        char.includes('people/18') ? count++ : count);
    });
    console.log(count);

    if (err) throw err;
  } catch {
    console.log(err);
  }
});
