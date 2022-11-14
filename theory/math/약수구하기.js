const num = 24;

// O(N^(1/2))
const findDivisors = (num) => {
  const divisors = [];

  for (let i = 1; i <= Math.floor(Math.sqrt(num)); i++) {
    if (num % i === 0) {
      divisors.push(i);

      if (i ** 2 != num) {
        divisors.push(num / i);
      }
    }
  }

  return divisors.sort((a, b) => a - b);
};

console.log(findDivisors(num).join(' '));
