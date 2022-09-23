from collections import deque
from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220924 17142 연구소 3

# 정답코드


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(queue):
    activated = []

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr_copy[nr][nc] == -10:
                    arr_copy[nr][nc] = arr_copy[r][c] + 1
                    queue.append((nr, nc))

                if arr_copy[nr][nc] == -2:
                    arr_copy[nr][nc] = arr_copy[r][c] + 1
                    activated.append((nr, nc))
                    queue.append((nr, nc))
                    

    for r in range(N):
        for c in range(N):
            if arr_copy[r][c] == -10:
                return sys.maxsize   
                
    for row, col in activated:
        arr_copy[row][col] = -2

    return max(map(max, arr_copy))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []


for r in range(N):
    for c in range(N):
        if arr[r][c] == 0:
            arr[r][c] = -10
        if arr[r][c] == 1:
            arr[r][c] = -1
        if arr[r][c] == 2:
            arr[r][c] = -2
            virus.append((r, c))


ans = sys.maxsize

for comb in combinations(virus, M):
    arr_copy = [arr[i][:] for i in range(N)]

    queue = deque()
    for loc in comb:
        queue.append(loc)
        r, c = loc
        arr_copy[r][c] = 0

    
    ans = min(bfs(queue), ans)
    # print(comb)
    # print(bfs(queue))
    # for row in arr_copy:
    #     print(row)
    
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)




