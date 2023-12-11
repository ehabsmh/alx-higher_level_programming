#!/usr/bin/node

const firstArg = Number(process.argv[2]);

if (!isNaN(firstArg)) console.log(`My number: ${parseInt(firstArg)}`);
else console.log('Not a number');
