# 220815 10814 나이순 정렬

import sys

input = sys.stdin.readline

N = int(input())

members = []

for _ in range(N):
    members.append(input().split())

# 파이썬의 기본 .sort 메소드(팀소트)는 안정정렬이므로 따로 작업을 해줄 필요가 없다.
members.sort(key= lambda x: int(x[0]))

for member in members:
    print(*member)

