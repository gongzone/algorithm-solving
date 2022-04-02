from itertools import count
import sys
getInput = sys.stdin.readline

n = int(getInput()) # 거슬러 줘야 할 돈
coin_types = [500, 100, 50, 10]
count = 0

for coin in coin_types:
  # 전부 다 거슬러 줬으면 for문 break
  if n == 0:
    break
  
  count += n // coin # 거슬러 준 횟수
  n %= coin # 거슬러 주고 남은 돈

print(count)
  