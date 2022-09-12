# 220912 1707 이분 그래프

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

K = int(input())


def bfs(start):

    queue = deque()
    visited[start] = 1
    queue.append((start, 1))

    while queue:
        start, mark = queue.popleft()
        # visited 부호를 바꿔줘서 기록
        for node in graph[start]:
            if visited[node] == 0:
                visited[node] = -mark
                queue.append((node, -mark))


def is_bipartite(visited):
    for i in range(1, V + 1):
        for adj in graph[i]:
            if visited[i] == visited[adj]:
                print('NO')
                return

    print('YES')
    return



for _ in range(K):
    V, E = map(int, input().split())
    # 그래프 만들기
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        node_1, node_2 = map(int, input().split())

        graph[node_1].append(node_2) 
        graph[node_2].append(node_1) 

    # 방문 표시
    visited = [0 for _ in range(V + 1)]

    # 미방문시 bfs
    for i in range(1, V + 1):
        if visited[i] == 0:
            bfs(i)
    
    # print(visited)
    # print(graph)
    is_bipartite(visited)


