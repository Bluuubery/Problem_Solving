# 220830 3055 탈출

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline
maxsize = sys.maxsize

# R, C: 숲 배열의 크기, forset: 숲 배열, water: 물의 확산과 확산속도를 담을 배열
R, C = map(int, input().split())
forest = [list(input().strip()) for _ in range(R)]
water = [[maxsize for _ in range(C)] for _ in range(R)]

# r_s, c_s: 고슴도치의 위치
# r_d, c_d: 비버의 위치
# water_queue: 물이 차있는 위치를 담은 큐
water_queue = deque()
for r in range(R):
    for c in range(C):
        if forest[r][c] == 'S':
            r_s, c_s = r, c
        elif forest[r][c] == 'D':
            r_d, c_d = r, c
        elif forest[r][c] == '*':
            water[r][c] = 0
            water_queue.append((r, c))


# 탐색 방향 설정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs_water(water_queue):
    while water_queue:
        r, c = water_queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and water[nr][nc] == maxsize:
                if forest[nr][nc] == '.' or forest[nr][nc] == 'S':
                    water[nr][nc] = water[r][c] + 1
                    water_queue.append((nr, nc))

def bfs_escape(r, c):
    queue = deque()
    queue.append((r, c))
    forest[r][c] = 0

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                # 탈출
                if forest[nr][nc] == 'D':
                    print(forest[r][c] + 1)
                    return
                # 물 시간 가능
                elif water[nr][nc] > forest[r][c] + 1:
                    if forest[nr][nc] == '.':
                        forest[nr][nc] = forest[r][c] + 1
                        queue.append((nr, nc))
    
    # 탈출 불가
    print('KAKTUS')
    return

bfs_water(water_queue)
bfs_escape(r_s, c_s)
