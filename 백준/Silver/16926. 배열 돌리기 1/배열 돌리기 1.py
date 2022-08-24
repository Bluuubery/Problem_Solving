# 220824 16926 배열 돌리기 1

# 정답 코드

import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        start = arr[x][y]

        for j in range(i + 1, N - i):
            x = j
            original = arr[x][y]
            arr[x][y] = start
            start = original

        for j in range(i + 1, M - i):
            y = j
            original = arr[x][y]
            arr[x][y] = start
            start = original

        for j in range(i + 1, N - i):
            x = N - j - 1
            original = arr[x][y]
            arr[x][y] = start
            start = original

        for j in range(i + 1, M - i):
            y = M - j - 1
            original = arr[x][y]
            arr[x][y] = start
            start = original

for row in arr:
    print(*row)