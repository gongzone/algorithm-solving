const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

const coin_types = [500, 100, 50, 10];

let n = parseInt(input);
let count = 0;

for (coin of coin_types) {
  if (n === 0) break;

  count += parseInt(n / coin);
  n %= coin;
}

console.log(count);
