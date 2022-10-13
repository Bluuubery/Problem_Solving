import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

# 델타 탐색 방향 설정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 아기 상어 먹이 거리 탐색 bfs
def bfs(shark_r, shark_c):
    # visited: 방문여부 & 먹이까지의 거리 표시할 배열
    visited = [[inf for _ in range(N)] for _ in range(N)]
    visited[shark_r][shark_c] = 0

    queue = deque()
    queue.append((shark_r, shark_c))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 조건 맞으면 거리 표시하면서 탐색
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == inf:
                # 먹이가 상어의 현재 크기보다 작거나 같은 경우
                if arr[nr][nc] <= shark:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
    
    # result: 먹을 수 있는 먹이까지의 거리와 좌표 (종료 조건을 위해 큰 값을 초기화)
    result = [(inf, inf, inf)]

    # 먹을 수 있는 먹이 (상어 현재 크기보다 작음) 거리와 좌표 담아주기
    for r in range(N):
        for c in range(N):
            if 0 < arr[r][c] < shark:
                result.append((visited[r][c], r, c))

    # 거리가 최소이면서 좌표가 왼쪽 위인 먹이의 정보 반환
    return min(result)


# N: 배열 크기, arr: 배열 정보
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 위치 찾아주기 및 탐색을 위한 좌표 초기화
for r in range(N):
    for c in range(N):
        if arr[r][c] == 9:
            shark_r, shark_c = r, c
            arr[r][c] = 0

inf = float('INF')
# shark: 상어 현재 크기, size_cnt: 먹은 먹이 개수
shark = 2
size_cnt = 0

# ans: 상어 이동 시간
ans = 0

while True:
    # 다음 먹이 정보 찾아주기
    time, next_r, next_c = bfs(shark_r, shark_c)

    # 먹이가 없으면 중단
    if time == inf:
        break
    
    # 먹이 먹기 및 해당 좌표로 상어 이동
    arr[next_r][next_c] = 0
    shark_r, shark_c = next_r, next_c

    # 정답 더해주기
    ans += time

    # 먹이 먹은 개수 세주기
    size_cnt += 1

    # 상어 크기 커지는 경우
    if size_cnt == shark:
        shark += 1
        size_cnt = 0

# 정답 출력
print(ans)
