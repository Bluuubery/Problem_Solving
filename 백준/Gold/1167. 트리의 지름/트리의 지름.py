# 220905 1167 트리의 지름

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N + 1)]
for _ in range(N):
    edge = list(map(int, input().split()))
    for i in range(1, len(edge) - 1, 2):
        tree[edge[0]].append([edge[i], edge[i + 1]])


def dfs(s):

    for edge in tree[s]:
        node = edge[0]
        weight = edge[1]
        if visited[node] == -1:
            visited[node] = visited[s] + weight
            dfs(node)

visited = [-1] * (N + 1)
visited[1] = 0
dfs(1)

s = visited.index(max(visited))
visited = [-1] * (N + 1)
visited[s] = 0
dfs(s)
print(max(visited))
