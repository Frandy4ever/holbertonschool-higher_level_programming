#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file.
const request = require('request');
const fileSys = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
request(url, function (err, response, body) {
  if (err) { console.error(err); }
  fileSys.writeFile(fileName, body, 'utf-8', function (err) {
    if (err) { console.error(err); }
  });
});
