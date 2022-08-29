# 220819 3003 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys

input = sys.stdin.readline

chess = [1, 1, 2, 2, 2, 8]

chess_input = list(map(int, input().split()))

for i in range(6):
    diff = chess[i] - chess_input[i]
    print(diff, end=' ')


