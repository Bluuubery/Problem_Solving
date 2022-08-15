# 220815 11650 좌표정렬하기

import sys

input = sys.stdin.readline

N = int(input())

coordinates = []

for _ in range(N):
    coordinates.append(list(map(int, input().split())))

coordinates.sort(key= lambda x: (x[0], x[1]))

for coordinate in coordinates:
    print(*coordinate)