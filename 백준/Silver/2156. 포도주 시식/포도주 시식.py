# 220821 10157 자리배정

import sys

input = sys.stdin.readline

# N: 포도주 잔 갯수, wine: 포도주 양
N = int(input())

wine = []
for _ in range(N):
    wine.append(int(input()))

# 3잔을 연속으로 마실 수 없으므로 3가지 경우의 수가 있다.
# (wine-1, wine-2), (wine, wine-2) (wine, wine -1)
# 점화식: max[i] = max(max[i - 1], wine[i] + max[i - 2], wine[i] + wine[i - 1] + max[i - 3])

# max_drink: 최대로 마실 수 있는 포도주의 양
max_drink = [0]
for i in range(N):
    # 초기항 설정
    if i == 0:
        max_drink.append(wine[0])
    elif i == 1:
        max_drink.append(wine[0] + wine[1])
    # 일반항 계산
    else:
        temp = max(max_drink[-1], wine[i] + max_drink[-2], wine[i] + wine[i - 1] + max_drink[-3])
        max_drink.append(temp)

print(max_drink[-1])
