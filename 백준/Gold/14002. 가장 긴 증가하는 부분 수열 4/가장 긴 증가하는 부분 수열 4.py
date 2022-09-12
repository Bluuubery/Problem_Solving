# 220912 14002 가장 긴 증가하는 부분 수열 4

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

dp = []
for i in range(N):
    if i == 0:
        dp.append(1)
    else:
        dp.append(1)
        for j in range(i):
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)

idx = max(dp)
lis = []
for i in range(N - 1, -1, -1):
    if dp[i] == idx:
        lis.append(numbers[i])
        idx -= 1
    
lis.reverse()

print(max(dp))
print(*lis)