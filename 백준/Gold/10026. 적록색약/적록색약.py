# 220913 10026 적록색약

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline



N = int(input())
arr = [list(map(str, input().strip())) for _ in range(N)]
arr_rgb = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B':
            arr_rgb[i][j] = 'B'
        else:
            arr_rgb[i][j] = 'R'

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, color, cnt):
    queue = deque()
    arr[r][c] = cnt
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == color:
                    arr[nr][nc] = cnt
                    queue.append((nr, nc))


def bfs_rgb(r, c, color, cnt):
    queue = deque()
    arr_rgb[r][c] = cnt
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr_rgb[nr][nc] == color:
                    arr_rgb[nr][nc] = cnt
                    queue.append((nr, nc))


cnt = 0
cnt_rgb = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'R' or arr[r][c] == 'G' or arr[r][c] == 'B':
            bfs(r, c, arr[r][c], cnt)
            cnt += 1

        if arr_rgb[r][c] == 'R' or arr_rgb[r][c] == 'G' or arr_rgb[r][c] == 'B':
            bfs_rgb(r, c, arr_rgb[r][c], cnt_rgb)
            cnt_rgb += 1

print(cnt, cnt_rgb)