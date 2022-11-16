const n = 2;
const strings = ['I am happy today', 'We want to win the first prize'];

const reverseWords = (string) => {
  const words = string.split(' ');
  return words.map((word) => word.split('').reverse().join('')).join(' ');
};

const solve = () => {
  const answer = [];

  for (let i = 0; i < n; i++) {
    answer.push(reverseWords(strings[i]));
  }

  return answer;
};

console.log(solve().join('\n'));
