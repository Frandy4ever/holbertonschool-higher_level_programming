#!/usr/bin/node
// Reads and prints the content of a file.
const fileSys = required('fileSys');
const file = process.argv[2];
fileSys.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
