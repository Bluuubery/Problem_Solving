from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220923 2589 보물섬

# 정답코드



def bfs(r, c):
    visited[r][c] = 0

    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] == 'L' and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

    return max(map(max, visited))

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0

for r in range(R):
    for c in range(C):
        if arr[r][c] == 'L':
            visited = [[-1 for _ in range(C)] for _ in range(R)]
            ans = max(ans, bfs(r, c))

print(ans)



