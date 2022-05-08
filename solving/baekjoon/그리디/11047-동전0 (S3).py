import sys
getInput = sys.stdin.readline

n, target = map(int, getInput().rstrip().rsplit())
coin_types = [int(getInput().rstrip()) for _ in range(n)]
count = 0

for i in range(len(coin_types)-1, -1, -1):
  if coin_types[i] > target:
    continue

  count += target // coin_types[i]
  target = target % coin_types[i]
  
  if target == 0:
    print(count)
    break
  




