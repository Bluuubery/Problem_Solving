# 220911 14502 연구소

# 정답코드

from collections import deque
from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

virus = deque()
safe = []
for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:
            virus.append((r, c))
        elif arr[r][c] == 0:
            safe.append((r, c))

wall_combs = list(combinations(safe, 3))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(new_walls, virus, arr):

    for r, c in new_walls:
        arr[r][c] = 1

    while virus:
        r, c = virus.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 2
                    virus.append((nr, nc))

    safe = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                safe += 1
    # print(arr)
    # for r, c in new_walls:
    #     arr[r][c] = 0            
    return safe


ans = 0
for walls in wall_combs:
    virus_copy = deepcopy(virus)
    arr_copy = deepcopy(arr)
    a = bfs(walls, virus_copy, arr_copy)
    if a > ans:
        ans = a
    # print(arr)

print(ans)