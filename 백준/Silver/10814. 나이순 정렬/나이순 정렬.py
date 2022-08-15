# 220815 10814 나이순 정렬

import sys

input = sys.stdin.readline

N = int(input())

members = []

for _ in range(N):
    members.append(input().split())

members.sort(key= lambda x: int(x[0]))

for member in members:
    print(*member)