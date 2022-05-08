import sys
import heapq
getInput = sys.stdin.readline

food_times = list(map(int, getInput().rstrip().split()))
k = int(getInput())

def solution(food_times, k):
  if sum(food_times) <= k:
    return -1
  
  heap = []
  
  for i in range(len(food_times)):
    heapq.heappush(heap, (food_times[i], i+1))

  prev = 0

  while True:
    now = heap[0][0]
    now_time = (now - prev) * len(heap)

    if now_time > k:
      break

    heapq.heappop(heap)[0]

    prev = now 
    k -= now_time
    
  heap.sort(key=lambda x: x[1])
  answer = heap[k % len(heap)][1]

  return answer

print(solution(food_times, k))