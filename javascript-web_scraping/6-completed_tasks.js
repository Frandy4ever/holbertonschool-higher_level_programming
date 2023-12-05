#!/usr/bin/node
// Computes the number of tasks completed by user id.
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.error(err); }
  const results = JSON.parse(body);
  const dict = {};
  for (const task of results) {
    if (task.completed === true) {
      if (task.userId in dict) {
        dict[task.userId]++;
      } else {
        dict[task.userId] = 1;
      }
    }
  }
  console.log(dict);
});
