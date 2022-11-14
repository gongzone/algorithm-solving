// let fs = require('fs');
// let inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const n = parseInt(inputs[0]);
// const nums = inputs[1].split(' ').map((num) => parseInt(num));

const n = 3;
const nums = [10, 20, 30];

const calculateAverage = (n, nums) => {
  const max = Math.max(...nums);
  return nums.reduce((acc, num) => acc + ((num / max) * 100) / n, 0);
};

console.log(calculateAverage(n, nums));
