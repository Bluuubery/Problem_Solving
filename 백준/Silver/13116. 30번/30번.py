# 220809 13116 30번

import sys

T = int(sys.stdin.readline())

for t in range(T):
    a, b = map(int, sys.stdin.readline().split())

    while True:
        if a == b:
            lca = a
            break

        elif a > b:
            a = a // 2

        elif a < b:
            b = b // 2
            
    print(lca * 10)