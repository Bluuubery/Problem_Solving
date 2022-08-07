#  220807 17298 오큰수

import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

nge = [-1] * n
stack = []

for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i]:
        nge[stack.pop()] = numbers[i]
    stack.append(i)

print(*nge)