# 220812 1012 유기농 배추

# 정답코드

from collections import deque
import sys

input = sys.stdin.readline

# 델타 탐색 방향 설정
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(a, b):

    cabbage[a][b] = 0
    q.append((a, b))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if cabbage[nr][nc] == 1:
                    cabbage[nr][nc] = 0
                    q.append((nr, nc))
                    # print(cabbage)
    

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbage = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()

    for _ in range(K):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    
    # print(cabbage)

    # bfs(0, 0)
    # print(cabbage)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)