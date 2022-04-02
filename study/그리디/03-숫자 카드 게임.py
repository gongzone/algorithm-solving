import sys
getInput = sys.stdin.readline

n, m = map(int, getInput().rstrip().split())
result = 0

for i in range(n):
  data = list(map(int, getInput().rstrip().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)