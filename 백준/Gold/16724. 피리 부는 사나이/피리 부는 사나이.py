import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221001 16724 피리 부는 사나이

# 정답코드

directions = {
    'D' : (1, 0),
    'U' : (-1, 0),
    'L' : (0, -1),
    'R' : (0, 1),
}


def dfs(r, c, r_start, c_start):

    if visited[r][c]:
        # print(f'merge: {r, c}')
        merge(r, c, r_start, c_start)
        return

    visited[r][c] = 1

    nr = r + directions[arr[r][c]][0]
    nc = c + directions[arr[r][c]][1]

    dfs(nr, nc, r_start, c_start)   

    # print(f'merge: {r, c}')
    merge(r, c, r_start, c_start)
    return


# find 함수
def find(x):
    if safezone[x] != x:
        safezone[x] = find(safezone[x])
    return safezone[x]


# union 함수
def merge(r_x, c_x, r_y, c_y):
    x = find((r_x * M) + c_x)
    y = find((r_y * M) + c_y)

    if x < y:
        safezone[y] = x
        
    else:
        safezone[x] = y

    return


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
safezone = [i for i in range(N * M)]

for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            dfs(r, c, r, c)
            # print(r, c)
            # for i in visited:
            #     print(i)


print(len(set(safezone)))

