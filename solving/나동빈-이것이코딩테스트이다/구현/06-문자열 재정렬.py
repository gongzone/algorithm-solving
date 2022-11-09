import sys
getInput = sys.stdin.readline

data = getInput().rstrip()
string = []
num = 0

for x in data:
  if x.isalpha():
    string.append(x)
  else:
    num += int(x)

sorted_string = ''.join(sorted(string))

if num == 0:
  print(sorted_string)
else:
  print(sorted_string + str(num))



