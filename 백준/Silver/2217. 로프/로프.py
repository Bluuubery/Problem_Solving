# 220904 2217 로프

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())
rope = []

for _ in range(N):
    rope.append(int(input()))

rope.sort()

max_weight = 0
for i in range(N):
    weight = rope[i] * (N - i)
    if weight > max_weight:
        max_weight = weight

print(max_weight)