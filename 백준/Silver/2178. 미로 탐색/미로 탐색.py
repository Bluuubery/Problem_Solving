# 220823 2173 미로탐색

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int,input().rstrip())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def boundary_check(row, col):
    if 0 <= row < N and 0 <= col < M:
        return True
    else: 
        return False

def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if boundary_check(next_row, next_col) and maze[next_row][next_col] == 1:
                maze[next_row][next_col] = maze[row][col] + 1
                queue.append((next_row, next_col))

    return maze[N - 1][M - 1]

print(bfs(0, 0))
