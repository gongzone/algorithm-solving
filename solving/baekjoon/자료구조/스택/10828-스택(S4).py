import sys
getInput = sys.stdin.readline

n = int(getInput())
stack = []

for _ in range(n):
  command = getInput().rstrip()
  
  if " " in command:
    stack.append(command.split()[1])

  if command == "pop":
    val = stack.pop() if len(stack) > 0 else -1
    print(val)
    continue

  if command == "size":
    print(len(stack))
    continue

  if command == "empty":
    val = 1 if len(stack) == 0 else 0
    print(val)
    continue

  if command == "top":
    val = stack[len(stack)-1] if len(stack) > 0 else -1
    print(val)
    continue