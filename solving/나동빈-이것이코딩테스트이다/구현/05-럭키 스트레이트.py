import sys
getInput = sys.stdin.readline

n = getInput().rstrip()
length = len(n)

total = 0

for i in range(length // 2):
  total += int(n[i])

for j in range(length // 2, length):
  total -= int(n[j])

if total == 0:
  print('LUCKY')
else:
  print('READY')