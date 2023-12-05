#!/usr/bin/node
// Write a string to a file
const fileSys = require('fs');
const file = process.argv[2];
const string = process.argv[3];
fileSys.writeFile(file, string, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
