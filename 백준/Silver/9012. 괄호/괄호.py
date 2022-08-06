# 220806 9012 괄호

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    stack = []
    ps = list(map(str, sys.stdin.readline()))
    for i in ps:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                stack.append(i)
                break
            else: stack.pop()
    if stack:
        print('NO')
    else: 
        print('YES')