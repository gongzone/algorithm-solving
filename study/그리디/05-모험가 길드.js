const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0]);
const adventurers = input[1].split(' ').map((el) => parseInt(el));
let count = 0;

adventurers.sort((a, b) => b - a);

for (let i = 0; i < adventurers.length; i++) {
  i += adventurers[i];
  count++;
}

console.log(count);
