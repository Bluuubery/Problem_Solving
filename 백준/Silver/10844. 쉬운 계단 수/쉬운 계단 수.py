# 220819 10844 쉬운 계단 수

import sys

input = sys.stdin.readline

N =int(input())

step = [[0] * 10 for _ in range(N)]

step[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if N == 1:
    print(sum(step[0]))
else:
    for i in range(1, N):
        step[i][0] = step[i - 1][1]
        for j in range(1, 9):
            step[i][j] = step[i - 1][j - 1] + step[i - 1][j + 1]
        step[i][9] = step[i - 1][8]

    ans = sum(step[N - 1]) % 1_000_000_000
    print(ans)

