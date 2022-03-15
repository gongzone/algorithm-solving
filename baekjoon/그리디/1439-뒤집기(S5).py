import sys
getInput = sys.stdin.readline

data = getInput().rstrip()
prev_num = int(data[0])
zero_count = 0
one_count = 0

if prev_num == 0:
  zero_count += 1
else:
  one_count += 1

for i in range(1, len(data)):
  num = int(data[i])
  
  if num != prev_num:
    if num == 1:
      one_count += 1
    else:
      zero_count += 1
    
    prev_num = num

print(min(zero_count, one_count))