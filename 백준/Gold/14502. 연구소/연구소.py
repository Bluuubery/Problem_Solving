# 220911 14502 연구소

# 정답코드

from collections import deque
from copy import deepcopy
from itertools import combinations
import sys
input = sys.stdin.readline

# N, M: 배열의 크기, arr: 배열
N, M = map(int, input().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# virus: bfs 탐색에서 바이러스의 위치를 담을 큐
# can_wall: 벽을 세울 수 있는 위치
virus = deque()
can_wall = []
for r in range(N):
    for c in range(M):
        if arr[r][c] == 2:
            virus.append((r, c))
        elif arr[r][c] == 0:
            can_wall.append((r, c))

# wall_combs: 벽을 세 울 수 있는 위치에서 3곳 고른 경우의 수
wall_combs = list(combinations(can_wall, 3))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# bfs 함수 선언
def bfs(new_walls, virus, arr):

    # 새로운 벽 설치
    for r, c in new_walls:
        arr[r][c] = 1

    # 바이러스 확산 bfs
    while virus:
        r, c = virus.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 2
                    virus.append((nr, nc))

    # safe: 안전 영역 크기
    safe = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                safe += 1
    
    # safe 반환
    return safe


# ans: 최대 안전 영역의 크기
ans = 0
# 경우의 수에 대해서 bfs 탐색 진행
for walls in wall_combs:
    virus_copy = deepcopy(virus)
    arr_copy = deepcopy(arr)
    # 최댓값 비교해가면서 갱신
    if ans < bfs(walls, virus_copy, arr_copy):
        ans = bfs(walls, virus_copy, arr_copy)

# 정답 출력
print(ans)