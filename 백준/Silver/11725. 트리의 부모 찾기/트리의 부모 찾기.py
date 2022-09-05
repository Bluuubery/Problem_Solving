# 220906 11725 트리의 부모 찾기

# 정답코드

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [-1] * (N + 1)

def dfs(s):
    for node in tree[s]:
        if visited[node] == -1:
            visited[node] = s
            dfs(node)

visited[1] = 0
dfs(1)

for i in range(2, N + 1):
    print(visited[i])