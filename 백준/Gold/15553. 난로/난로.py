# 220813 15553 난로

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

friends = []
for _ in range(N):
    arrive = int(input())
    friends.append([arrive, arrive + 1])

gap = []
for i in range(1, N):
    gap.append(friends[i][0] - friends[i - 1][1])

gap.sort(reverse=True)
# print(gap)
total_gap = sum(gap[:K - 1])
# print(total_gap)
time = friends[-1][1] - friends[0][0] - total_gap

print(time)