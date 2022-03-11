import sys
import math

def era_sieve(n):
  array = [True] * (n + 1)

  for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
      j = 2

      while i * j <= n:
        array[i * j] = False
        j += 1

  return array

sieved_array = era_sieve(1000000)

for line in sys.stdin:
  target = int(line)

  if target == 0:
    break

  i = 2
  j = target - 2

  try:
    while sieved_array[i] == False or sieved_array[j] == False:
      i += 1
      j -= 1
  except:
    print("Goldbach's conjecture is wrong")
    continue

  print(f"{target} = {i} + {j}")
