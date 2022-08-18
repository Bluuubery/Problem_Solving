# 220818 1149 RGB거리

import sys

input = sys.stdin.readline

N = int(input())

rgb = [[0, 0, 0] for _ in range(N)]

rgb_input = []
for _ in range(N):
    rgb_input.append(list(map(int, input().split())))

rgb[0]= rgb_input[0]

for i in range(1, N):
    rgb[i][0] = rgb_input[i][0] + min(rgb[i - 1][1], rgb[i - 1][2])
    rgb[i][1] = rgb_input[i][1] + min(rgb[i - 1][0], rgb[i - 1][2])
    rgb[i][2] = rgb_input[i][2] + min(rgb[i - 1][0], rgb[i - 1][1])

# print(rgb)
print(min(rgb[N - 1]))
