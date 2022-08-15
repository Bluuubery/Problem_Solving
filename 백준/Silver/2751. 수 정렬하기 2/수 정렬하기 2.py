# 220815 2751 수 정렬하기 2

import sys

input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

for number in numbers:
    print(number)