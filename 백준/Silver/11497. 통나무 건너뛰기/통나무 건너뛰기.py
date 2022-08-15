# 220814 11497 통나무 건너뛰기

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    
    gap = list()
    gap.append(logs[1] - logs[0])
    for i in range(2, N):
        gap.append(logs[i] - logs[i - 2])

    print(max(gap))
