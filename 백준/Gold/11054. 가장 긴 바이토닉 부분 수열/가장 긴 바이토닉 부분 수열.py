# 220823 11054 가장 긴 바이토닉 부분 수열

import sys

input = sys.stdin.readline

# N: 수열의 길이, numbers: 수열, reversed_numbers: 뒤집은 수열
N = int(input())
numbers = list(map(int, input().split()))
reversed_numbers = numbers[::-1]

# lis, lds: 가장 긴 증가/감소 부분 수열을 담을 리스트
lis = []
lds = []
for i in range(N):
    # 모든 수열은 기본적으로 1의 길이를 가진다.(초기항 = 1)
    if i == 0:
        lis.append(1)
        lds.append(1)
    else:
        lis.append(1)
        lds.append(1)
        # 탐색하는 숫자보다 작은 숫자에 대해 탐색하면서 lis와 lds를 갱신한다.
        for j in range(i):
            if numbers[i] > numbers[j]:
                lis[i] = max(lis[i], lis[j] + 1)
            if reversed_numbers[i] > reversed_numbers[j]:
                lds[i] = max(lds[i], lds[j] + 1)

# lds 리스트를 뒤집어서 lis 리스트와 더하고 1을 빼준다(자기 자신)
lds.reverse()
lbs = [lis[i] + lds[i] - 1 for i in range(N)]

print(max(lbs))
