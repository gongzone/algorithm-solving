import sys
getInput= sys.stdin.readline

n = int(getInput()) # 테스트 케이스 개수

for _ in range(n):
  m = int(getInput()) # 전화번호 수
  p = [getInput().rstrip() for _ in range(m)] # 전화번호 목록이 담긴 리스트
  p.sort()

  start = p[0]
  answer = 'YES'

  for i in range(1, m):
    if p[i].startswith(start):
      answer = 'NO'
      break

    start = p[i]

  print(answer)

