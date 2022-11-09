import sys
getInput = sys.stdin.readline

n, m = map(int, getInput().rstrip().split())
x, y, direction = map(int, getInput().rstrip().split())

visit_map = [[0] * m for _ in range(n)]
visit_map[x][y] = 1
count = 1
turn_time = 0

# 북, 동, 남, 서
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

game_map = []
for _ in range(n):
  game_map.append(list(map(int, getInput().rstrip().split())))

def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

while True:
  turn_left()
  nx = x + moves[direction][0]
  ny = y + moves[direction][1]

  if visit_map[nx][ny] == 0 and game_map[nx][ny] == 0:
    x = nx
    y = ny
    visit_map[x][y] = 1
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1

  if turn_time == 4:
    nx = x - moves[direction][0]
    ny = y - moves[direction][1]

    if game_map[nx][ny] == 0:
      x = nx
      y = ny
      turn_time = 0
    else:
      break

print(count)

