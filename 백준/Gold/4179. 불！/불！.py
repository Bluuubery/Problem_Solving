# 220829 4179 불!

# 정답코드

from collections import deque
from re import L
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]
fire = [[99999 for _ in range(C)] for _ in range(R)]

def find_index(x, maze):
    for i in range(R):
        for j in range(C):
            if maze[i][j] == x:
                return i, j

def bfs_fire(fire_q, maze):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while fire_q:
        r, c = fire_q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C and fire[nr][nc] == 99999:
                if maze[nr][nc] == '.' or maze[nr][nc] == 'J':
                    fire[nr][nc] = fire[r][c] + 1
                    fire_q.append((nr, nc))
    
    
    return


def bfs_escape(r, c, maze):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque()
    queue.append((r, c))
    maze[r][c] = 0

    while queue:
        r, c = queue.popleft()

        if r == 0 or r == R - 1 or c == 0 or c == C - 1:
            print(maze[r][c] + 1)
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                if fire[nr][nc] > maze[r][c] + 1:
                    if maze[nr][nc] == '.':
                        maze[nr][nc] = maze[r][c] + 1
                        queue.append((nr, nc))

    
    print('IMPOSSIBLE')
    return 

fire_q = deque()

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            fire[i][j] = 0
            fire_q.append((i, j))


bfs_fire(fire_q, maze)
r_j, c_j = find_index('J', maze)
bfs_escape(r_j, c_j, maze)

# for row in fire:
#     print(*row)
# print()
# for row in maze:
#     print(*row)
    