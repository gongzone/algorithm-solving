import sys
getInput = sys.stdin.readline

n, m, k = map(int, getInput().rstrip().split()) # 배열의 크기, 숫자가 더해지는 횟수, 연속으로 더해질 수 있는 횟수
array = list(map(int, getInput().rstrip().split()))

array.sort(reverse=True)

first = array[0]
second = array[1]

first_num = k * (m // k)
second_num = m % k

answer = first * first_num + second * second_num
print(answer)

