# 220821 2628 종이자르기

import sys

input = sys.stdin.readline

W, H = map(int, input().split())
N = int(input())

width_cut, height_cut = [0], [0]

for _ in range(N):
    cut = list(map(int, input().split()))

    if cut[0] == 0:
        width_cut.append(cut[1])
    else:
        height_cut.append(cut[1])

width_cut.sort()
height_cut.sort()

width_cut.append(H)
height_cut.append(W)

width, height = [], []

for i in range(1, len(width_cut)):
    width.append(width_cut[i] - width_cut[i - 1])
for j in range(1, len(height_cut)):
    height.append(height_cut[j] - height_cut[j - 1])

# print(width_cut, height_cut)
# print(width, height)

print(max(width) * max(height))

