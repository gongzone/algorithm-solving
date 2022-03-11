import sys

getInput = sys.stdin.readline

n = int(getInput())

flowers = []

# 인풋 값 계산하기 편한 형식으로 변경
for _ in range(n):
  input_data = list(map(int, getInput().rstrip().split()))
  blooming_day = input_data[0] * 100 + input_data[1]
  falling_day = input_data[2] * 100 + input_data[3]
  flowers.append((blooming_day, falling_day))

flowers.sort() # 오름차순으로 정렬

def get_min_flower_number():
  target_day = 301 # 3월 1일, loop가 진행되며 점진적으로 증가
  end_day = 1130 # 11월 30일
  
  total_number = 0 # 3월 1일부터 11월 30일까지 꽃이 피어있게 하기위한 꽃의 최소한의 수
  memo_day = 0 # 아직 지켜볼 여지가 있는 상황을 위해 저장해놓은 날짜

  for i in range(n):
    # target_day가 end_day를 넘어서면 loop 중지
    if target_day > end_day:
      break

    flower_birth = flowers[i][0]
    flower_death = flowers[i][1]
    
    # 해당 꽃의 피고 지는 범위가 target_day를 감쌀 때 (해당 꽃이 필요한 꽃으로 등록할 가능성이 있는 상황)
    if flower_birth <= target_day and flower_death > target_day:
      
      # 해당 꽃의 탄생일이 저장해놓은 날짜 보다 큰 경우 (지켜볼 여지가 없음, 바로 필요한 꽃으로 등록(+1))
      if flower_birth > memo_day:
        memo_day = target_day 
        target_day = flower_death
        total_number += 1

      # 지켜볼 여지가 있음, target_day만 증가
      else:
        target_day = flower_death

    # 해당 꽃이 필요한 꽃으로 등록할 가능성이 없는 상황 (범위를 벗어남)
    else:

      # 꽃의 탄생일이 target_day를 넘는 경우 연속성이 끊기기 때문에 loop 중지 
      if flower_birth > target_day:
        total_number = 0
        break
  
  # loop 종료 후 target_day가, 11월 30일보다 같거나 적을 경우 빈 영역이 생기기 때문에 0 값을 리턴할 준비
  if target_day <= end_day:
    total_number = 0

  return total_number

result = get_min_flower_number()
print(result)