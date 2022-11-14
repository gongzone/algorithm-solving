// N 이하의 자연수 중에서 k를 약수로 갖는 개수는 N/k 이다.

const num = 10000;

const getDivisorSum = (num) => {
  let answer = 0;

  for (let i = 1; i <= num; i++) {
    answer += i * Math.floor(num / i);
  }

  return answer;
};

console.log(getDivisorSum(num));
