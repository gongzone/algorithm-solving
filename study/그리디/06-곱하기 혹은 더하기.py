import sys
getInput = sys.stdin.readline

n = getInput().rstrip()

result = int(n[0])

for i in range(1, len(n)):
  now = int(n[i])
  
  if result > 1 and now > 1:
    result *= now 
  else:
    result += now

print(result)
