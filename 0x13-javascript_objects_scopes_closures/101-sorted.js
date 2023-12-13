#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (let i = 0; i < Object.entries(dict).length; i++) {
  const key = Object.entries(dict)[i][0];
  const value = Object.entries(dict)[i][1];

  if (!(value in newDict)) newDict[value] = [];

  newDict[value].push(key);
}
console.log(newDict);
