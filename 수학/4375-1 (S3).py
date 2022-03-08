import sys

getInput = sys.stdin.readline

while True:
  try:
    num = int(getInput().rstrip())
    comparing = 1
    count = 1

    while True:
      if comparing % num == 0:
        print(len(str(num)))
        break
      else:
        comparing += 10 ** count

      count += 1
  except:
    break