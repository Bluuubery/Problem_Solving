# 220821 10157 자리배정

import sys

input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
else:
    direction_x = [0, 1, 0, -1]
    direction_y = [1, 0, -1, 0]

    seat = [[0 for _ in range(R)] for _ in range(C)]

    x = 0
    y = 0
    d = 0

    for k in range(1, K):
        seat[x][y] = k

        x += direction_x[d]
        y += direction_y[d]

        if not(0 <= x < C and 0 <= y < R and seat[x][y] == 0):
            x -= direction_x[d]
            y -= direction_y[d]

            d = (d + 1) % 4
            x += direction_x[d]
            y += direction_y[d]

    print(x + 1, y + 1)
