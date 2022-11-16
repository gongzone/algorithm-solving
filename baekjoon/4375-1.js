// 모듈러 연산 참고,
// (A + B) % p = ((A % p) + (B % p)) % p
// (A * B) % p = ((A % p) * (B % p)) % p
// 이해 안가는 문제...

// const nums = require('fs')
//   .readFileSync('/dev/stdin')
//   .toString()
//   .trim()
//   .split('\n')
//   .map((num) => parseInt(num));

const nums = [3, 7, 9901];

const calculateMinDigit = (num) => {
  if (num === 1) return 1;

  let comparing = 1;
  let count = 1;

  while (comparing !== 0) {
    comparing = (comparing * 10 + 1) % num;
    count++;
  }

  return count;
};

console.log(nums.map((num) => calculateMinDigit(num)).join('\n'));
