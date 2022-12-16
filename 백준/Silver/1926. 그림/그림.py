import sys, os, io, atexit
from collections import deque

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221216 1926 그림

# 정답코드

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0
max_size = 0

def bfs(r, c):
    global max_size

    queue = deque()

    queue.append((r, c))
    visited[r][c] = True
    size = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and paper[nr][nc] == 1:
                    size += 1
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    
    max_size = max(max_size, size)

for r in range(N):
    for c in range(M):
        if paper[r][c] == 1 and not visited[r][c]:
            cnt += 1
            bfs(r, c)

print(cnt)
print(max_size)
