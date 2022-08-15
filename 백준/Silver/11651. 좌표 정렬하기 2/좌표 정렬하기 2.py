# 220815 11651 좌표 정렬하기2

import sys

input = sys.stdin.readline

N = int(input())

coordinates = []

for _ in range(N):
    coordinates.append(list(map(int, input().split())))

# 람다를 이용해 y좌표를 첫번째 키로, x좌표를 두번째 키로 정렬한다.
coordinates.sort(key= lambda x: (x[1], x[0]))

for coordinate in coordinates:
    print(*coordinate)