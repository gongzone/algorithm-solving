const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0][0]);
const m = parseInt(input[0][2]);
const k = parseInt(input[0][4]);
const array = input[1].split(' ').map((el) => parseInt(el));

array.sort((a, b) => b - a);

const fisrt = array[0];
const second = array[1];

const firstNum = k * Math.trunc(m / k);
const secondNum = m % k;

const answer = fisrt * firstNum + second * secondNum;
console.log(answer);
