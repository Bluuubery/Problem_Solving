# 10828 스택
def push(x):
    stack.append(x)
    return

def pop():
    if stack:
        return stack.pop()
    else:
        return -1

def size():
    return len(stack)

def empty():
    if stack:
        return 0
    else:
        return 1

def top():
    if stack:
        return stack[-1]
    else:
        return -1

import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    order = sys.stdin.readline().split()
    funct = order[0]

    if funct == 'push':
        push(order[1])
    elif funct == 'pop':
        print(pop())
    elif funct == 'size':
        print(size())
    elif funct == 'empty':
        print(empty())
    elif funct == 'top':
        print(top())
