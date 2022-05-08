import sys
getInput = sys.stdin.readline

s = getInput().rstrip()

prev = int(s[0])
zero_count = 0
one_count = 0

for i in range(1, len(s)):
  now = int(s[i])
  
  if prev != now:
    if now == 1:
      zero_count += 1
    else:
      one_count += 1
  
  prev = now

print(min(zero_count, one_count))

