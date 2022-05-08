import sys
import heapq

getInput = sys.stdin.readline
INF = int(1e9) # int max값

v, e = map(int, getInput().rstrip().split()) # v: 노드의 개수, e: 간선의 개수
k = int(getInput().rstrip()) # 시작 노드

graph = [[] for _ in range(v+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 2차원 리스트
distance = [INF] * (v+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보 입력받기
for _ in range(e):
  a, b, c = map(int, getInput().rstrip().split()) # a 노드에서 b 노드로 가는데 가중치가 c
  graph[a].append((b,c)) # a 노드에 b를 연결하고 가중치 정보도 포함

def dijkstra(start_node):
  queue = []
  heapq.heappush(queue, (0, start_node)) # 시작 노드로 가기 위한 최단 거리는 0, 큐에 삽입
  distance[start_node] = 0 # 마찬가지로 시작노드 최단 거리는 0

  # 큐가 완전히 빌 때까지 반복문 수행
  while queue:
    dist, node = heapq.heappop(queue) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

    # 현재 노드가 전에 처리되었다면 continue
    if distance[node] < dist: 
      continue

    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[node]:
      cost = dist + i[1] # 현재 노드 최단 거리 + 연결된 노드와의 거리
      
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))

# 다익스트라 수행
dijkstra(k)

# 모든 노드로 가기 위한 최단거리를 출력
for i in range(1, v+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])

