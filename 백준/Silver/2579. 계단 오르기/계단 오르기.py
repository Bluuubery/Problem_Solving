# 220818 2579 계단 오르기

import sys

input = sys.stdin.readline

# t[k][0] = t[k-1][2] + score (안 건너뜀)
# t[k][1] =  max(t[k-2][0], t[k-2][1]) + score (건너 뜀)
# max(t[k][0], t[k][1])

N = int(input())

stair = []
for _ in range(N):
    stair.append(int(input()))

score = [[0] * 2 for _ in range(N)]

if N == 1:
    score[0][0] = stair[0]
    score[0][1] = 0
elif N == 2:
    score[0][0] = stair[0]
    score[0][1] = 0
    score[1][0] = stair[0] + stair[1]
    score[1][1] = stair[1]
else:
    score[0][0] = stair[0]
    score[0][1] = 0
    score[1][0] = stair[0] + stair[1]
    score[1][1] = stair[1]
    for i in range(2, N):
        score[i][0] = score[i - 1][1] + stair[i]
        score[i][1] = max(score[i - 2][0], score[i - 2][1]) + stair[i]

score_max = []
for score_pair in score:
    score_max.append(max(score_pair))

# print(score)
print(score_max[N - 1])