# 220827 2206 벽 부수고 이동하기

# 정답코드

from collections import deque
from copy import deepcopy
import sys
intput = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
arr2 = deepcopy(arr)
arr_3d = [arr, arr2]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(z, r, c):

    arr_3d[z][r][c] = 1
    queue = deque()
    queue.append((z, r, c))
    
    while queue:

        z, r, c = queue.popleft()
        
        if r == N - 1 and c == M - 1:
            # for i in arr_3d:
            #     print()
            #     for row in i:
            #         print(*row)

            print(arr_3d[z][r][c])
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:

                if arr_3d[z][nr][nc] == 1:
                    if z == 0:
                        arr_3d[1][nr][nc] = arr_3d[0][r][c] + 1
                        queue.append((1, nr, nc))
                    
                elif arr_3d[z][nr][nc] == 0:
                    arr_3d[z][nr][nc] = arr_3d[z][r][c] + 1
                    queue.append((z, nr, nc)) 

    print(-1)
    # for i in arr_3d:
    #     print()
    #     for row in i:
    #         print(*row)
    return

# print(arr_3d)
bfs(0, 0, 0)
