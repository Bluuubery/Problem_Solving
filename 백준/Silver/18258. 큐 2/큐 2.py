# 220809 10828 스택

import sys
from collections import deque


def push(x):
    q.append(x)
    return

def pop():
    if q:
        return q.popleft()
    else:
        return -1

def size():
    return len(q)

def empty():
    if q:
        return 0
    else:
        return 1

def front():
    if q:
        return q[0]
    else:
        return -1

def back():
    if q:
        return q[-1]
    else:
        return -1


n = int(sys.stdin.readline())
q = deque()

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
    elif funct == 'front':
        print(front())
    elif funct == 'back':
        print(back())
