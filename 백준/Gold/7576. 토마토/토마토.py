# 220827 7576 토마토

# 정답코드

from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0,  0]
dc = [0, 0, -1, 1]

def bfs(queue):
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if tomato[nr][nc] == 0:
                    tomato[nr][nc] = tomato[r][c] + 1
                    queue.append((nr, nc))

queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

bfs(queue)

flag = True

max_tomato = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            flag = False
            break
        elif tomato[i][j] > max_tomato:
            max_tomato = tomato[i][j]

if flag:
    print(max_tomato - 1)
else:
    print(-1)