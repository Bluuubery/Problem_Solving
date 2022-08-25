# 220812
# 24479 알고리즘 수업 - 깊이 우선 탐색 1

# 정답코드

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(V, E, R):
    global visited
    global cnt

    visited[R] = cnt

    for x in E[R]:
        if visited[x] == 0:
            cnt += 1
            dfs(V, E, x)


V, M, R = map(int, input().split())

E = [[] for _ in range(V + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)


for edge in E:
    edge.sort()

visited = [0 for _ in range(V + 1)]
cnt = 1

dfs(V, E, R)

for i in range (1, V + 1):
    print(visited[i])

    