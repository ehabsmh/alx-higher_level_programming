#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);
const square = 'X';

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    console.log(square.repeat(squareSize));
  }
}
