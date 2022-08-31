# 220831 11047 동전 0

# 정답코드

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0
for coin in coins:
    cnt += K // coin
    K = K % coin
    if K == 0:
        break

print(cnt)
