from collections import deque
from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220924 17141 연구소 2

# 정답코드

# 델타 탐색 방향 설정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 바이러스 확산 bfs
def bfs(queue):
    while queue: 
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                # 빈 곳이거나 바이러스를 놓을 수 있는 곳이면 확산 시간을 표시하면서 탐색한다.
                if arr_copy[nr][nc] == -10 or arr_copy[nr][nc] == -2:
                    arr_copy[nr][nc] = arr_copy[r][c] + 1
                    queue.append((nr, nc))

    # 바이러스 확산 후 빈 공간이 남아있으면 확산 시간 초기화
    for r in range(N):
        for c in range(N):
            if arr_copy[r][c] == -10:
                return sys.maxsize   

    # 확산 시간 반환
    return max(map(max, arr_copy))


# N: 연구소의 크기, M: 바이러스의 개수
N, M = map(int, input().split())
# arr: 연구소 상태
arr = [list(map(int, input().split())) for _ in range(N)]
# virus: 바이러스를 놓을 위치
virus = []

# 빈 공간을 -10으로 초기화해주고 바이러스의 위치를 담아준다.
for r in range(N):
    for c in range(N):
        if arr[r][c] == 0:
            arr[r][c] = -10
        if arr[r][c] == 1:
            arr[r][c] = -1
        if arr[r][c] == 2:
            arr[r][c] = -2
            virus.append((r, c))

# ans: 바이러스 전체 확산 시간 (충분히 큰 값으로 초기화)
ans = sys.maxsize

# 바이러스를 놓을 위치를 고른다.
for comb in combinations(virus, M):
    # arr_copy: bfs 탐색용 배열 복사본
    arr_copy = [arr[i][:] for i in range(N)]

    # 바이러스의 위치 큐에 담아주기
    queue = deque()
    for loc in comb:
        queue.append(loc)
        r, c = loc
        arr_copy[r][c] = 0

    # 정답 갱신해가면서 bfs 탐색
    ans = min(bfs(queue), ans)

# 다 확산 시키지 못할 경우 -1 출력
if ans == sys.maxsize:
    print(-1)
# 정답 출력
else:
    print(ans)




