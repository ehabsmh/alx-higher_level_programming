#!/usr/bin/node

const process = require('process');
const request = require('request');

let apiUrl = process.argv.slice(2, 3);

if (apiUrl.length) {
  apiUrl = apiUrl.toString();
} else {
  console.log('Usage: ./0-readme.js apiUrl');
  process.exit(1);
}

request.get(apiUrl, { json: true }, (err, res, body) => {
  try {
    const movies = body.results;
    const moviesByChar = [];

    movies.forEach(movie => {
      const x = movie.characters.filter(char =>
        char.includes('people/18'));
      moviesByChar.push(...x);
    });

    console.log(moviesByChar.length);

    if (err) throw err;
  } catch {
    console.log(err);
  }
});
