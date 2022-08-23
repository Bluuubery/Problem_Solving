# 220821 11722 가장 긴 감소하는 부분 수열

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

lds = []
for i in range(N):
    if i == 0:
        lds.append(1)
    else:
        lds.append(1)
        for j in range(i):
            if numbers[i] < numbers[j]:
                lds[i] = max(lds[i], lds[j] + 1)

print(max(lds))
