import sys
getInput = sys.stdin.readline

n = int(getInput())
count = 0

for hour in range(n + 1):
  for minute in range(60):
    for seconds in range(60):
      if '3' in str(hour) + str(minute) + str(seconds):
        count += 1

print(count)