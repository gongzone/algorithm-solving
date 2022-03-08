import sys

for line in sys.stdin:
  num = int(line)
  comparing = 1
  count = 1

  if num == 1:
    print(1)
    break

  while comparing != 0:
    comparing = (comparing * 10 + 1) % num
    count += 1
  
  print(count)