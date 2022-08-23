# 220816 2491 수열

import sys

input = sys.stdin.readline

N = int(input())

numbers = tuple(map(int, input().split()))

max_cnt = 1
cnt = 1
for i in range(len(numbers) - 1):
    if numbers[i + 1] >= numbers[i]:
        cnt += 1
    else:
        cnt = 1

    if cnt > max_cnt:
        max_cnt = cnt

numbers = numbers[::-1]

cnt = 1
for i in range(len(numbers) - 1):
    if numbers[i + 1] >= numbers[i]:
        cnt += 1
    else:
        cnt = 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
