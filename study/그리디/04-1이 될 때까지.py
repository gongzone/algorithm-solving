import sys
getInput = sys.stdin.readline

n, k = map(int, getInput().rstrip().split())
result = 0

while True:
  # k로 나누어 떨어지는 수가 될 때까지 1씩 빼기
  target = (n // k) * k
  result += (n - target)
  n = target

  # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break

  # k로 나누기
  n //= k
  result += 1

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
