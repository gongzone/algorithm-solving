import sys
getInput = sys.stdin.readline

n = int(getInput())
commands = getInput().rstrip().split()

moves = {
  "L": (0, -1),
  "R": (0, 1),
  "U": (-1, 0),
  "D": (1, 0)
}

positions = [1, 1]

for i in range(len(commands)):
  nx = moves[commands[i]][0] + positions[0]
  ny = moves[commands[i]][1] + positions[1]

  if nx < 1 or nx > n or ny < 1 or ny > n:
    continue

  positions[0] = nx
  positions[1] = ny
  
print(positions[0], positions[1])
