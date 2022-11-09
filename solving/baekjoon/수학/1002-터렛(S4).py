import sys
import math
getInput = sys.stdin.readline

t = int(getInput())

for _ in range(t):
  x1, y1, r1, x2,  y2, r2 = map(int, getInput().rstrip().split())
  distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  answer = 0

  if distance == 0:
    answer = -1 if r1 == r2 else 0
  else:
    if r1 + r2 == distance or abs(r1 - r2) == distance:
      answer = 1
    elif abs(r1 - r2) < distance and r1 + r2 > distance:
      answer = 2
    else:
      answer = 0
  
  print(answer)
  