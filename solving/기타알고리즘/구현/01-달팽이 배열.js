const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const makeSnailArray = (n, snail_array) => {
  let num = 0;
  let row = 0;
  let col = -1;
  let inc = 1;

  while (n > 0) {
    for (let i = 0; i < n; i++) {
      num++;
      col += inc;
      snail_array[row][col] = num;
    }

    n--;

    for (let j = 0; j < n; j++) {
      num++;
      row += inc;
      snail_array[row][col] = num;
    }

    inc *= -1;
  }
};

const solution = (line) => {
  const n = parseInt(line);
  const snail_array = Array.from({ length: n }, () => Array(n).fill(0));

  makeSnailArray(n, snail_array);

  console.log(snail_array);
  rl.close();
};

rl.on("line", solution).on("close", () => process.exit());
