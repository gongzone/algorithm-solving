const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0]);
const graph = input.slice(1, n + 1).map((el) => el.split(''));
const counts = [];

const dfs = (x, y) => {
  if (x >= n || x < 0 || y >= n || y < 0) return 0;
  if (+graph[x][y] === 0) return 0;

  let count = 1;
  graph[x][y] = 0;

  count += dfs(x, y + 1) + dfs(x, y - 1) + dfs(x + 1, y) + dfs(x - 1, y);
  return count;
};

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    const result = dfs(i, j);

    result > 0 && counts.push(result);
  }
}

counts.sort((a, b) => {
  return +a - +b;
});

console.log(counts.length);
for (let x of counts) console.log(x);
