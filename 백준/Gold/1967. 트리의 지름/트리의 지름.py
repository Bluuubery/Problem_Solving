# 220828 1967 트리의 지름

# 정답코드

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N + 1)]
visited = [-1 for _ in range(N + 1)]

for _ in range(N - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])


def dfs(s):
    for edge in tree[s]:
        node = edge[0]
        weight = edge[1]
        if visited[node] == -1:
            visited[node] = visited[s] + weight
            # print(visited)
            dfs(node)

visited[1] = 0
dfs(1)
# print(visited)

s = visited.index(max(visited))
# print(s)
visited = [-1 for _ in range(N + 1)]
visited[s] = 0
dfs(s)
# print(visited)
print(max(visited))




