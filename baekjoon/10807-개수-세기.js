// let fs = require('fs');
// let inputs = fs.readFileSync('/dev/stdin').toString().split('\n');

// const nums = inputs[1].split(' ').map((num) => parseInt(num));
// const target = parseInt(inputs[2]);

const nums = [1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4];
const target = 2;

function getNumberOfTarget(nums, target) {
  console.log(nums.filter((num) => num === target).length);
}

getNumberOfTarget(nums, target);
