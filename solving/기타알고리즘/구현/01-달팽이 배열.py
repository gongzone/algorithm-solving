import sys
getInput = sys.stdin.readline

n = int(getInput())
snail_array = [[0] * n for _ in range(n)]

def print_snail_array(snail_array):
  length = len(snail_array)
  for i in range(length):
    print(snail_array[i][:length])

def make_snail_array(n, snail_array):
  num = 0
  row = 0
  col = -1
  inc = 1

  while n > 0:

    for _ in range(n):
      col += inc
      num += 1
      snail_array[row][col] = num

    n -= 1

    for _ in range(n):
      row += inc
      num += 1
      snail_array[row][col] = num

    inc *= -1

make_snail_array(n, snail_array)

print_snail_array(snail_array)


