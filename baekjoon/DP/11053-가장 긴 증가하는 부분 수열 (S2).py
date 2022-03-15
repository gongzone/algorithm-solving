import sys
from bisect import bisect_left

getInput = sys.stdin.readline

n = int(getInput().rstrip())
sequence = list(map(int, getInput().rstrip().split()))

# lis -> dynamic programming
# Time Complexity: O(n2).  
def lis(sequence):
  dp = [1 for _ in range(n)]

  for i in range(1, n):
    for j in range(0, i):
      if sequence[i] > sequence[j] and dp[i] < dp[j]+1:
        dp[i] = dp[j] + 1

  maximum = 0

  for i in range(n):
    maximum = max(maximum, dp[i])

  return maximum

# lis -> binary search
# Time Complexity: O(nlogn).

def lis_BS(sequence):
  table = [0 for _ in range(n)]
  length = 0

  table[0] = sequence[0]
  length = 1
  for i in range(1, n):
    if sequence[i] > table[length-1]:
      table[length] = sequence[i]
      length += 1
    else:
      table[bisect_left(table, sequence[i], 0, length-1 )] = sequence[i]

  return length

solution = lis_BS(sequence)
print(solution)

