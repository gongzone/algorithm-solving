import sys
import heapq

getInput = sys.stdin.readline
INF = int(1e9)

n = int(getInput()) # 도시의 개수
m = int(getInput()) # 버스의 개수

graph = [[] for _ in range(n+1)]
costs = [INF] * (n+1)

for _ in range(m):
  # a: 출발 도시, b: 도착 도시, c: 버스 비용
  a, b, c = map(int, getInput().rstrip().split())
  graph[a].append((b,c))

# 구하고자 하는 구간의 출발점, 도착점
start_city, end_city = map(int, getInput().rstrip().split())

def dijkstra(start_city):
  queue = []
  heapq.heappush(queue, (0, start_city))
  costs[start_city] = 0

  while queue:
    cost_now, node = heapq.heappop(queue)

    if costs[node] < cost_now:
      continue

    for x in graph[node]:
      cost_extended = cost_now + x[1] 

      if cost_extended < costs[x[0]]:
        costs[x[0]] = cost_extended
        heapq.heappush(queue, (cost_extended, x[0]))

dijkstra(start_city)

print(costs[end_city])