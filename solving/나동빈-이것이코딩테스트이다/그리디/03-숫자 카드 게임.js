const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0][0]);
let result = 0;

for (let i = 1; i <= n; i++) {
  const data = input[i].split(' ').map((el) => parseInt(el));
  const min_value = Math.min.apply(null, data);
  result = Math.max(result, min_value);
}

console.log(result);
