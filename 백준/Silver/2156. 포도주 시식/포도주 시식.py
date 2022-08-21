# 220821 10157 자리배정

import sys

input = sys.stdin.readline

N = int(input())

wine = []
for _ in range(N):
    wine.append(int(input()))

max_drink = [0]
for i in range(N):
    if i == 0:
        max_drink.append(wine[0])
    elif i == 1:
        max_drink.append(wine[0] + wine[1])
    else:
        temp = max(max_drink[-1], wine[i] + max_drink[-2], wine[i] + wine[i - 1] + max_drink[-3])
        max_drink.append(temp)

# print(max_drink)
print(max_drink[-1])
