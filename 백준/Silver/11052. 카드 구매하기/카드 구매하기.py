# 220823 11052 카드 구매하기

import sys

input = sys.stdin.readline

# N: 구매할 카드 개수, card: 카드팩 가격 
N = int(input())
card = [0] + list(map(int, input().split()))

# dp 저장 테이블
dp = [0 for _ in range(N + 1)]

# dp[i] = max(dp[i], dp[i - k] + card[k])
for i in range(N + 1):
    for k in range(i + 1):
        dp[i] = max(dp[i], dp[i - k] + card[k])

# 정답 출력
print(dp[i])
