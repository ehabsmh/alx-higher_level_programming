#!/usr/bin/node

const fileSys = require('fs');

let argv = process.argv;

argv = argv.slice(2);
const srcFile1 = argv[0];
const srcFile2 = argv[1];
const destFile = argv[2];

const arr = [srcFile1, srcFile2];

for (let i = 0; i < arr.length; i++) {
  fileSys.readFile(arr[i], 'utf8', (err, data) => {
    if (err) console.log(err);

    fileSys.appendFile(destFile, data, (err) => {
      if (err) console.log(err);
    });
  });
}
