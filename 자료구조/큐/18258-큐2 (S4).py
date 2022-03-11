import sys
from collections import deque

getInput = sys.stdin.readline

n = int(getInput())
q = deque()

for _ in range(n):
  command = getInput().rstrip()

  if " " in command:
    num = command.split()[1]
    q.append(num)
    continue

  if command == "pop":
    val = q.popleft() if len(q) > 0 else -1
    print(val)
    continue

  if command == "size":
    print(len(q))
    continue

  if command == "empty":
    val = 1 if len(q) == 0 else 0
    print(val)
    continue

  if command == "front":
    val = q[0] if len(q) > 0 else -1
    print(val)
    continue

  if command == "back":
    val = q[len(q) - 1] if len(q) > 0 else -1
    print (val)
    continue
  
