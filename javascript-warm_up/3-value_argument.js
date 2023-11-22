#!/usr/bin/node
const sysArgs = process.argv.length - 2;

if (sysArgs === 0) {
    console.log('No argument');
}else {
    console.log(sysArgs[1]);
}
