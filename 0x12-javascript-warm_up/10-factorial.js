#!/usr/bin/node
function fact (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

console.log(fact(Number(process.argv[2])));
