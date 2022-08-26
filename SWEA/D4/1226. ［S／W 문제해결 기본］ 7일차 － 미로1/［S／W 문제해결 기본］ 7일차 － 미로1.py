# 220825
# 1226 미로1

# 정답코드

from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j


def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            n_r = r + dr[i]
            n_c = c + dc[i]

            if 0 <= n_r < 16 and 0 <= n_c < 16 and maze[n_r][n_c] != 1:
                if maze[n_r][n_c] == 3:
                    return 1
                elif maze[n_r][n_c] == 0:
                    maze[n_r][n_c] = '*'
                    queue.append((n_r, n_c))

    return 0


for _ in range(10):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    start_r, start_c = find_start(maze)
    print('#{} {}'.format(T, bfs(start_r, start_c)))
