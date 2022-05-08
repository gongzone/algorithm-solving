import sys
getInput = sys.stdin.readline

n, m = map(int, getInput().rstrip().split())
visited = [False] * (n+1)
stack = []

def explore(depth):
  if depth > m:
    print(' '.join(map(str, stack)))
    return

  for i in range(1, n+1):
    if not visited[i]:
      visited[i] = True
      stack.append(i)

      explore(depth + 1)
      
      visited[i] = False
      stack.pop()

explore(1)


