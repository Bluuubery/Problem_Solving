# 220818 2579 계단 오르기

import sys

input = sys.stdin.readline

# t[k][0] = t[k-1][2] + score (안 건너뜀)
# t[k][1] =  max(t[k-2][0], t[k-2][1]) + score (건너 뜀)
# max(t[k][0], t[k][1])

N = int(input())

# stair: 각 계단의 점수
stair = []
for _ in range(N):
    stair.append(int(input()))

# 각 계단별 점수 조합
score = [[0] * 2 for _ in range(300)]

# 점화식 초기항
score[0][0] = stair[0]
score[0][1] = 0
if N >= 2:
    score[1][0] = stair[0] + stair[1]
    score[1][1] = stair[1]

if N >= 3:
    for i in range(2, N):
        score[i][0] = score[i - 1][1] + stair[i]
        score[i][1] = max(score[i - 2][0], score[i - 2][1]) + stair[i]

# 최대 점수만을 리스트에 담아준다.
score_max = []
for score_pair in score:
    score_max.append(max(score_pair))

print(score_max[N - 1])

# N번째 값만을 찾을 거면 다음과 같은 방식도 된다. (더 빠름)
# score_max = max(score[N - 1])
# print(score_max)
