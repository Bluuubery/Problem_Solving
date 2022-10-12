from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221012 16236 아기상어

# 정답코드


def bfs(r, c):
    visited = [[0 for _ in range(N)] for _ in range(N)]

    visited[r][c] = 1

    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0:
                    if arr[nr][nc] == 9:
                        return visited[r][c]

                    if arr[nr][nc] <= shark:
                        visited[nr][nc] = visited[r][c] + 1
                        queue.append((nr, nc))

    return float('inf')



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            shark_r, shark_c = r, c

shark = 2
size_cnt = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0

while True:
    distance = float('inf')

    for r in range(N):
        for c in range(N):
            if 0 < arr[r][c] < shark:
                if bfs(r, c) < distance:
                    next_r, next_c = r, c
                    distance = bfs(r, c)

    if distance == float('inf'):
        break
    
    arr[shark_r][shark_c] = 0
    arr[next_r][next_c] = 9

    shark_r, shark_c = next_r, next_c

    ans += distance

    size_cnt += 1
    if size_cnt == shark:
        shark += 1
        size_cnt = 0
    
    # for row in arr:
    #     print(row)
    # print(shark, distance)
    # print()

print(ans)


