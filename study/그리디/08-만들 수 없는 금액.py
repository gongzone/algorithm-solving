import sys
getInput = sys.stdin.readline

n = int(getInput())
coins = list(map(int, getInput().rstrip().split()))
coins.sort()

target = 1
for x in coins:
  if target < x:
    break

  target += x

print(target)