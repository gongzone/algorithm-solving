import sys
getInput = sys.stdin.readline

# 지도의 크기(n x n) 입력받기
n = int(getInput()) 

# 지도 채우기
graph = []
for _ in range(n):
  graph.append(list(map(int, getInput().rstrip())))

# 연결된 노드들의 개수 리스트
counts = []

def dfs(x, y):
  # 종료 컨디션(범위를 벗어날때, 해당노드의 값이 0일 때)
  if x >= n or x < 0 or y >= n or y < 0:
    return 0
  
  if graph[x][y] == 0:
    return 0

  graph[x][y] = 0 # 방문했으니 다음번 방문하지 않기 위해 0으로 처리
  count = 1 

  # 상,하,좌,우 dfs 순회를 통해 해당 노드와 연결된 노드들의 개수 구하기
  count += dfs(x, y+1) + dfs(x, y-1) + dfs(x+1, y) + dfs(x-1, y) 
  return count 

# 각각의 노드들마다 dfs 실행
for i in range(n):
  for j in range(n):
    result = dfs(i, j)
    if result > 0:
      counts.append(result)

# 솔루션 출력
print(len(counts))
for x in sorted(counts):
  print(x)