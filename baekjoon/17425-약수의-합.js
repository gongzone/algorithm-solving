const inputs = [5, 1, 2, 10, 70, 10000];

const MAX_LENGTH = 1000000;

const calculateDp = () => {
  const dp = Array.from({ length: MAX_LENGTH + 1 }).fill(0);

  for (let i = 1; i <= MAX_LENGTH; i++) {
    for (let j = 1; i * j <= MAX_LENGTH; j++) {
      dp[i * j] += i;
    }

    dp[i] += dp[i - 1];
  }

  return dp;
};

const solve = () => {
  const answer = [];

  const dp = calculateDp();

  for (let i = 1; i <= parseInt(inputs[0]); i++) {
    const num = parseInt(inputs[i]);
    answer.push(dp[num]);
  }

  return answer;
};

console.log(solve().join('\n'));
