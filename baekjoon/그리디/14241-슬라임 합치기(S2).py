import sys
getInput = sys.stdin.readline

n = int(getInput())
slimes = list(map(int, getInput().rstrip().split()))
slimes.sort(reverse=True)

sum = 0
score = 0

for i in range(len(slimes) - 1):
  sum = slimes[i] + slimes[i+1]
  score += slimes[i] * slimes[i+1]
  slimes[i+1] = sum

print(score)

