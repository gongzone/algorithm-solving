import sys
getInput = sys.stdin.readline

pos = getInput().rstrip()
row = int(pos[1])
col = ord(pos[0]) - ord('a') + 1

moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
count = 0

for move in moves:
  nx = row + move[0]
  ny = col + move[1]

  if nx < 1 or nx > 8 or ny < 1 or ny > 8:
    continue

  count += 1

print(count)

