# 220827 7576 토마토

# 정답코드

from collections import deque
import sys

input = sys.stdin.readline

# 탐색 방향 설정
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def bfs(queue):

    while queue:
        h, r, c = queue.popleft()
        # 3차원 탐색
        for i in range(6):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nh < H and 0 <= nr < N and 0<= nc < M:
                if tomato[nh][nr][nc] == 0:
                    tomato[nh][nr][nc] = tomato[h][r][c] + 1
                    queue.append((nh, nr, nc))



M, N, H = map(int, input().split())

tomato = []
for _ in range(H):
    tomato.append([list(map(int, input().split())) for _ in range(N)])

queue = deque()

for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[h][r][c] == 1:
                queue.append((h, r, c))

bfs(queue)

ripe = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato[h][r][c] == 0:
                print(-1)
                exit(0)
            elif tomato[h][r][c] > ripe:
                ripe = tomato[h][r][c]
print(ripe - 1)
