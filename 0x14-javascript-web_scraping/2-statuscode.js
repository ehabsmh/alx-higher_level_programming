#!/usr/bin/node

const process = require('process');
const request = require('request');

let url = process.argv.slice(2, 3);

if (url.length) {
  url = url.toString();
} else {
  console.log('Usage: ./2-statuscode.js URL');
  process.exit(1);
}

request.get(url, (_, res, body) => {
  console.log('code:', res.statusCode);
});
