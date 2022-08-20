# 220821 2605 줄 세우기

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

student = []
for i in range(N):
    student.insert(i - numbers[i], i + 1)

print(*student)
