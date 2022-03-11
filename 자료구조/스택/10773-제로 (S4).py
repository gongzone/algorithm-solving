import sys
getInput = sys.stdin.readline

k = int(getInput())
stack = []

for _ in range(k):
  num = int(getInput())

  if num != 0:
    stack.append(num)
  else:
    stack.pop()

print(sum(stack))

