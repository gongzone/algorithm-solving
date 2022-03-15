import sys

getInput = sys.stdin.readline

test = int(getInput().rstrip())
n = [int(getInput().rstrip()) for _ in range(test)]

dp = [(1, 0), (0, 1)]

for i in range(2, max(n)+1):
  dp.append(tuple(sum(elem) for elem in zip(dp[i-1], dp[i-2])))

for i in n:
  print(' '.join(map(str, dp[i])))

