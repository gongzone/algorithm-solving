import sys
getInput = sys.stdin.readline

n = int(getInput())
adventurers = list(map(int, getInput().rstrip().split()))

adventurers.sort(reverse=True)
i = 0
count = 0

while True:
  i += adventurers[i]
  count += 1

  if i > len(adventurers)-1:
    break

print(count)