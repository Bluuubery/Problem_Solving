import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
sys.setrecursionlimit(10**6)

# 221216 2583 영역 구하기

# 정답코드

R, C, K = map(int, input().split())

arr = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(K):
    rectangle = list(map(int, input().split()))
    for r in range(rectangle[1], rectangle[3]):
        for c in range(rectangle[0], rectangle[2]):
            arr[r][c] = 1


cnt = 0
result = []

visited = [[False for _ in range(C)] for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    global size
    
    visited[r][c] = True

    if not arr[r][c]:
        size += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and not arr[r][c]:
                visited[nr][nc] = True
                dfs(nr, nc)


for r in range(R):
    for c in range(C):
        if arr[r][c] == 0 and not visited[r][c]:
            cnt += 1
            size = 0

            dfs(r, c)

            result.append(size)

print(cnt)
print(*sorted(result))
