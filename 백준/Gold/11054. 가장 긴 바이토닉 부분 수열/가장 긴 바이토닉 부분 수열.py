# 220823 11054 가장 긴 바이토닉 부분 수열

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

# lis: 가장 긴 부분 수열을 담을 리스트
lis = []
for i in range(N):
    # 모든 수열은 기본적으로 1의 길이를 가진다.(초기항 = 1)
    if i == 0:
        lis.append(1)
    else:
        lis.append(1)
        # 탐색하는 숫자보다 작은 숫자에 대해 탐색하면서 lis를 갱신한다.
        for j in range(i):
            if numbers[i] > numbers[j]:
                lis[i] = max(lis[i], lis[j] + 1)

numbers = numbers[::-1]
lds = []
for i in range(N):
    # 모든 수열은 기본적으로 1의 길이를 가진다.(초기항 = 1)
    if i == 0:
        lds.append(1)
    else:
        lds.append(1)
        # 탐색하는 숫자보다 작은 숫자에 대해 탐색하면서 lis를 갱신한다.
        for j in range(i):
            if numbers[i] > numbers[j]:
                lds[i] = max(lds[i], lds[j] + 1)

lds = lds[::-1]

lbs = [lis[i] + lds[i] for i in range(N)]

print(max(lbs) - 1)