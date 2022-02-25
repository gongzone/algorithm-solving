import sys
from collections import deque

getInput = sys.stdin.readline

n, m, v = map(int, getInput().rstrip().split()) # n: 노드의 갯수, m: 간선의 개수, v: 시작 노드
graph = [[] for _ in range(n+1)] # 빈 2차원 리스트 생성(그래프)
visited_dfs = [False] * (n+1) # dfs를 통해 방문한 노드인지 확인하기 위한 1차원 리스트
visited_bfs = [False] * (n+1) # bfs를 통해 방문한 노드인지 확인하기 위한 1차원 리스트

# 간선 정보 입력받고 그래프에 추가
for _ in range(m):
  a, b = map(int, getInput().rstrip().split())

  # a,b 노드 연결
  graph[a].append(b)
  graph[b].append(a)

# 그래프에 연결된 노드들 오름차순으로 정렬
for i in graph:
  i.sort()

# dfs 선언
def dfs(v):
  visited_dfs[v] = True # 방문한 노드로 기록
  print(v, end=" ") # 방문했으니 해당 노드 출력

  # 해당 노드에 연결된 노드들 반복문을 통해 검사
  for i in graph[v]:
    if not visited_dfs[i]: # 연결된 노드가 방문하지 않았던 경우 
      dfs(i) # 재귀적으로 연결된 노드 dfs 실행

# bfs 선언
def bfs(v):
  queue = deque([v]) # queue 선언, 시작 노드값 넣어줌
  visited_bfs[v] = True # 시작 노드 방문한 노드로 기록

  # queue가 빌 때까지 반복문 수행
  while queue:
    now = queue.popleft() # dequeue
    print(now, end= " ") # 뺀 노드 출력

    # 해당 노드에 연결된 노드들 반복문을 통해 검사
    for i in graph[now]:
      if not visited_bfs[i]: # 연결된 노드가 방문하지 않았던 경우 
        queue.append(i) # enqueue
        visited_bfs[i] = True # 연결된 노드 방문한 노드로 기록

# dfs, bfs 호출
dfs(v)
print()
bfs(v)





