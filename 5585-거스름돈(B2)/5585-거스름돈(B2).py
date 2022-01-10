# 그리디 - 거스름돈 문제
# 핵심: 가장 큰 화폐 단위부터 잔돈으로 지급

import sys

getInput = sys.stdin.readline

price = int(getInput())
n = 1000 - price

coins = [500, 100, 50, 10, 5, 1]

result = 0

for coin in coins:
    result += n // coin
    n %= coin

    if n == 0:
        break

print(result)
