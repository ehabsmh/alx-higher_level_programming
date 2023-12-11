#!/usr/bin/node
const { argv } = require('node:process');

argv.splice(0, 2);

if (!argv.length) console.log('No argument');
else if (argv.length === 1) console.log('Argument found');
else console.log('Arguments found');
