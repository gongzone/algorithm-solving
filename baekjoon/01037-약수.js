// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
// const nums = inputs[1].split(' ');

const nums = [14, 26456, 2, 28, 13228, 3307, 7, 23149, 8, 6614, 46298, 56, 4, 92596];

const getDivisor = (nums) => {
  const min = Math.min(...nums);
  const max = Math.max(...nums);

  return min * max;
};

console.log(getDivisor(nums));
