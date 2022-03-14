import sys
getInput = sys.stdin.readline

target = 1000 - int(getInput())
coin_types = [500, 100, 50, 10, 5, 1]
count = 0

for x in coin_types:
  if target >= x:
    count += target // x
    target = target % x

  if target == 0:
    break

print(count)

