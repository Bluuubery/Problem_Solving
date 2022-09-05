# 220905 14889 스타트와 링크

# 정답코드

from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
player = [i for i in range(N)]

team_comb = list(combinations(player, N//2))

min_diff = 999999
for i in range(len(team_comb)):
    team_1 = team_comb[i]
    team_2 = list(set(player) - set(team_1))

    stats_1 = 0
    stats_2 = 0
    for j in range(N//2):
        for k in range(j, N//2):
            stats_1 += arr[team_1[j]][team_1[k]]
            stats_1 += arr[team_1[k]][team_1[j]]

            stats_2 += arr[team_2[j]][team_2[k]]
            stats_2 += arr[team_2[k]][team_2[j]]

    stat_diff = abs(stats_1 - stats_2)

    if stat_diff < min_diff:
        min_diff = stat_diff

print(min_diff)
