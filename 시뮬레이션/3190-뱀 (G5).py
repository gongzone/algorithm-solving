import sys
from collections import deque

getInput = sys.stdin.readline

n = int(getInput())
apple_num = int(getInput())
board = [[0] * (n + 1) for _ in range(n + 1)]
direction_hash = {}

for _ in range(apple_num):
  apple_x, apple_y = map(int, getInput().rstrip().split())
  board[apple_x][apple_y] = 1

direction_num = int(getInput())

for _ in range(direction_num):
  time, direction = getInput().rstrip().split()
  direction_hash[time] = direction

class Snake:
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  def __init__(self):
    self.x = 1
    self.y = 1
    self.direction = 0

  def turn(self, change):
    if change == "L":
      self.direction = (self.direction -1) % 4
    else:
      self.direction = (self.direction + 1) % 4
  
  def move(self):
    self.x += self.dx[self.direction]
    self.y += self.dy[self.direction]

def simulate():
  snake = Snake()
  board[snake.x][snake.y] = 2
  q = deque() 
  q.append(((snake.x, snake.y)))
  step = 0
  
  while True:
    snake.move()
    step += 1

    # 벽에 부딪히면 종료
    if snake.x > n or snake.y > n or snake.x == 0 or snake.y == 0:
      return step

    # 머리와 몸통이 맞닿으면 종료
    if board[snake.x][snake.y] == 2:
      return step

    # 움직였을 때 해당 자리에 사과가 없으면 꼬리 부분 삭제 
    if board[snake.x][snake.y] == 0:
      tail_x, tail_y = q.popleft()
      board[tail_x][tail_y] = 0

    # 머리가 위치한 자리 기록 && 큐에 추가
    board[snake.x][snake.y] = 2
    q.append((snake.x, snake.y))

    # 방향 전환이 이루어지는 타이밍 때, 방향 전환 수행
    if str(step) in direction_hash:
      snake.turn(direction_hash[str(step)])

print(simulate())