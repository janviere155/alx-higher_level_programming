#!/usr/bin/node
const nm = Math.floor(Number(process.argv[2]));
if (isNaN(nm)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${nm}`);
}
