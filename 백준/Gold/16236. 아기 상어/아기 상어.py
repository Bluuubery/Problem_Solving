import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(shark_r, shark_c):
    visited = [[inf for _ in range(N)] for _ in range(N)]
    visited[shark_r][shark_c] = 0

    queue = deque()
    queue.append((shark_r, shark_c))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == inf:
                if arr[nr][nc] <= shark:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
    
    result = [(inf, inf, inf)]
    for r in range(N):
        for c in range(N):
            if 0 < arr[r][c] < shark:
                result.append((visited[r][c], r, c))

    return min(result)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            shark_r, shark_c = r, c
            arr[r][c] = 0

inf = float('INF')
shark = 2
size_cnt = 0

ans = 0

while True:
    time, next_r, next_c = bfs(shark_r, shark_c)

    if time == inf:
        break
    
    arr[next_r][next_c] = 0

    shark_r, shark_c = next_r, next_c

    ans += time
    size_cnt += 1
    if size_cnt == shark:
        shark += 1
        size_cnt = 0

print(ans)
