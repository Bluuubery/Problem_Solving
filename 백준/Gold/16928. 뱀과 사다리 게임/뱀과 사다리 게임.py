# 220912 16928 뱀과 사다리 게임

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ladder_snake = {i : i for i in range(1, 101)}

for _ in range(N + M):
    start, end = map(int, input().split())
    ladder_snake[start] = end

visited = [0 for _ in range(101)]


def bfs(start):
    
    visited[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()

        for i in range(1, 7):
            nx = ladder_snake[x + i]
            if visited[nx] == 0:
                if nx == 100:
                    # print(visited)
                    print(visited[x])
                    return
                elif 1 <= nx <100:
                    # print(nx, x, visited[x])
                    visited[nx] = visited[x] + 1
                    queue.append(nx)


# print(visited)
bfs(1)