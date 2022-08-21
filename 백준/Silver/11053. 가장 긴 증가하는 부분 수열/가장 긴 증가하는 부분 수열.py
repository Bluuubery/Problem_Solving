# 220821 11053 가장 긴 증가하는 부분 수열

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

lis = []
for i in range(N):
    if i == 0:
        lis.append(1)
    else:
        lis.append(1)
        for j in range(i):
            if numbers[i] > numbers[j]:
                lis[i] = max(lis[i], lis[j] + 1)

# print(lis)
print(max(lis))
