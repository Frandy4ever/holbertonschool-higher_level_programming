#!/usr/bin/node

const cLArguments = process.argv[2];
const sizeAsInt = parseInt(cLArguments);

if (!isNaN(sizeAsInt)) {
  for (let i = 0; i < sizeAsInt; i++) {
    let counter = '';
    for (let j = 0; j < sizeAsInt; j++) {
      counter += 'X';
    }
    console.log(counter);
  }
} else {
  console.log('Missing size');
}
