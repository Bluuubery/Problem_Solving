from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220921 18405 경쟁적 감염

# 정답코드

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

virus = []

for r in range(N):
    for c in range(N):
        if arr[r][c]:
            virus.append((r, c, arr[r][c], 0))

virus = deque(sorted(virus, key=lambda x: x[2]))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(virus=deque):

    while virus:
        r, c, virus_type, time = virus.popleft()
        if time == S:
            print(arr[X - 1][Y - 1])
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = virus_type
                    virus.append((nr, nc, virus_type, time + 1))

    print(arr[X - 1][Y - 1])
    return


bfs(virus)