import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221001 16724 피리 부는 사나이

# 정답코드

# directions: 방향 정보 저장
directions = {
    'D' : (1, 0),
    'U' : (-1, 0),
    'L' : (0, -1),
    'R' : (0, 1),
}


# dfs를 통해 safezone 연결
def dfs(r, c, r_start, c_start):

    # 이전에 탐색한 곳이면
    if visited[r][c]:
        # 유니온파인드 함수를 통해 재귀적으로 safezone과 연결해준다
        merge(r, c, r_start, c_start)
        return

    # 방문 표시
    visited[r][c] = 1

    # 다음 탐색 좌표
    nr = r + directions[arr[r][c]][0]
    nc = c + directions[arr[r][c]][1]

    # 재귀적으로 탐색
    dfs(nr, nc, r_start, c_start)   

    # 함수 basecondition 도달 이후 재귀적으로 safezone 연결
    merge(r, c, r_start, c_start)
    return


# find 함수
def find(x):
    if safezone[x] != x:
        safezone[x] = find(safezone[x])
    return safezone[x]


# union 함수
def merge(r_x, c_x, r_y, c_y):

    # 2차원 배열의 좌표를 1차원 형태로 변환
    x = find((r_x * M) + c_x)
    y = find((r_y * M) + c_y)

    if x < y:
        safezone[y] = x
        
    else:
        safezone[x] = y

    return


# N, M: 배열의 크기
N, M = map(int, input().split())
# arr: 지도 배열 
arr = [list(input()) for _ in range(N)]

# visited: 방문여부 표시 배열
visited = [[0 for _ in range(M)] for _ in range(N)]
# safezone: 유니온파인드 집합 표시 배열
safezone = [i for i in range(N * M)]

# 방문하지 않은 곳이 있으면 dfs를 통해서 safezone과 연결해준다.
for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            dfs(r, c, r, c)

# safezone의 개수 출력
print(len(set(safezone)))

