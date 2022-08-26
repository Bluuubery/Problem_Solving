# 220827 7576 토마토

# 정답코드

from collections import deque
import sys

input = sys.stdin.readline

# 탐색 방향 설정
dr = [-1, 1, 0,  0]
dc = [0, 0, -1, 1]

# bfs 함수 선언: 여러 개의 시작점(tomato[r][c] == 1)에서 동시에 시작하는 bfs
def bfs(queue):
    
    while queue:
        r, c = queue.popleft()
        # 4방향 bfs
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위를 벗어나지 않고 익지 않은 토마토면 거리 표시 후 탐색
            if 0 <= nr < N and 0 <= nc < M:
                if tomato[nr][nc] == 0:
                    tomato[nr][nc] = tomato[r][c] + 1
                    queue.append((nr, nc))

# M: 가로 길이(열), N: 세로 길이(행), tomato: 토마토 배열
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

# queue: 시작점을 담을 큐
# 시작점(토마토 == 1)들을 큐에 담아준다.
queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))

# 시작점들에 대하여 bfs 실시
bfs(queue)

# ripe: 토마토가 익는데 걸리는 최소 일수
ripe = 0
for i in range(N):
    for j in range(M):
        # 안 익은 토마토가 있으면 -1을 출력하고 코드 종료
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
        # 최댓값(bfs에서의 최댓값은 전체 탐색의 최소거리(최소 일수)이다)을 비교하면서 갱신한다
        elif tomato[i][j] > ripe:
            ripe = tomato[i][j]

# 1에서 시작했으므로 1을 빼준 값을 정답으로 출력한다.
print(ripe - 1)
