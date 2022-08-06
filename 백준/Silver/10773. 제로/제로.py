# 220806 10773 제로

import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    m = int(sys.stdin.readline())
    if m:
        stack.append(m)
    else:
        stack.pop()


print(sum(stack))