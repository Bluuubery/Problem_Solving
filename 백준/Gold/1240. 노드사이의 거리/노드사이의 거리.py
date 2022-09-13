# 220913 1240 노드사이의 거리

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node_1, node_2, weight = map(int, input().split())
    tree[node_1].append([node_2, weight])
    tree[node_2].append([node_1, weight])


def bfs(start, end):
    visited[start] = 0

    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node == end:
            print(visited[node])
            return

        for next, weight in tree[node]:
            if visited[next] == -1:
                visited[next] = visited[node] + weight
                queue.append(next)

    print(visited[node])
    return


for _ in range(M):
    start, end = map(int, input().split())
    visited = [-1 for _ in range(N + 1)]
    bfs(start, end)