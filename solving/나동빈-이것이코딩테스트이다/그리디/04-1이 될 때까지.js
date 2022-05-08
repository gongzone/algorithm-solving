const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

let n = parseInt(input[0]);
const k = parseInt(input[1]);
let result = 0;

while (true) {
  const target = parseInt(n / k) * k;
  result += n - target;
  n = target;

  if (n < k) break;

  n /= k;
  result += 1;
}

result += n - 1;
console.log(result);
