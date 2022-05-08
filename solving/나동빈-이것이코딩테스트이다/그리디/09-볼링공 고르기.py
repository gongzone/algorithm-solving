import sys
getInput = sys.stdin.readline

n, m = map(int, getInput().rstrip().split())
bowlings = list(map(int, getInput().rstrip().split()))

hash_map = {}
result = 0

for x in bowlings:
  if x not in hash_map:
    hash_map[x] = 0

  hash_map[x] += 1

for i in range(1, m):
  n -= hash_map[i]
  result += n * hash_map[i]

print(result)