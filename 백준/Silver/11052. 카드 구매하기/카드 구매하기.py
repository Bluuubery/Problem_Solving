# 220823 11052 카드 구매하기

import sys

input = sys.stdin.readline

N = int(input())
card = [0] + list(map(int, input().split()))

dp = [0 for _ in range(N + 1)]

for i in range(N + 1):
    for k in range(i + 1):
        dp[i] = max(dp[i], dp[i - k] + card[k])

print(dp[i])
