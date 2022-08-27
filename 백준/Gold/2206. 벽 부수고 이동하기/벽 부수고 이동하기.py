# 220827 2206 벽 부수고 이동하기

# 정답코드

from collections import deque
from copy import deepcopy
import sys
intput = sys.stdin.readline

# N: 행의 개수, M: 열의 개수
N, M = map(int, input().split())

# arr: 맵, arr2: arr의 복사본 (2차원 배열이므로 deepcopy)
arr = [list(map(int, input())) for _ in range(N)]
arr2 = deepcopy(arr)
# arr_3d: 맵의 3차원 배열 (0: 벽 안 부숨, 1: 벽 부숨)
arr_3d = [arr, arr2]

# 탐색 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 3차원 bfs 함수 선언
def bfs(z, r, c):

    # 출발점 표시
    arr_3d[z][r][c] = 1
    
    # queue: 좌표를 담을 큐
    queue = deque()
    queue.append((z, r, c))
    
    while queue:
        z, r, c = queue.popleft()
        
        # 목표 지점 도착 시 거리 출력 후 반환
        if r == N - 1 and c == M - 1:
            print(arr_3d[z][r][c])
            return

        # 4방향 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 탐색 방향이 인덱스 범위를 벗어나지 않을 때
            if 0 <= nr < N and 0 <= nc < M:

                # 벽이 있을 경우
                if arr_3d[z][nr][nc] == 1:
                    # 아직 벽을 부수지 않았을 경우 벽을 부수고 벽을 부순 차원으로 넘어가서 탐색을 진행한다.
                    if z == 0:
                        arr_3d[1][nr][nc] = arr_3d[0][r][c] + 1
                        queue.append((1, nr, nc))
                
                # 벽이 없을 경우 현재 차원에서 그대로 탐색을 진행한다.
                elif arr_3d[z][nr][nc] == 0:
                    arr_3d[z][nr][nc] = arr_3d[z][r][c] + 1
                    queue.append((z, nr, nc)) 
    
    # 목표 지점에 도착하지 못했을 경우 -1 출력 후 반환
    print(-1)
    return

# bfs 탐색 실시
bfs(0, 0, 0)
