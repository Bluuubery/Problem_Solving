# 220913 4803 트리

# 정답코드

import sys
input = sys.stdin.readline


def dfs(node, parent):
    visited[node] = 1

    for child in graph[node]:
        if visited[child] == 1:
            if child != parent:
                return False

        if visited[child] == 0:
            if not dfs(child, node):
                return False
    
    return True



T = 1
while True:
    N, M = map(int, input().split())
    if N == 0 and M ==0:
        exit()

    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        parent, child = map(int, input().split())
        graph[parent].append(child)
        graph[child].append(parent)
    
    visited = [0 for _ in range(N + 1)]

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            if dfs(i, 0):
                cnt += 1

    if cnt > 1:
        print(f'Case {T}: A forest of {cnt} trees.')
    elif cnt == 1:
        print(f'Case {T}: There is one tree.')
    else:
        print(f'Case {T}: No trees.')
    
    T += 1