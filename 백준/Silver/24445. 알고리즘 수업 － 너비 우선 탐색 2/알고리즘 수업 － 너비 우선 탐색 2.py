# 220825 24445 알고리즘 수업 - 너비 우선 탐색 2

from collections import deque
import sys

input = sys.stdin.readline


def bfs(V, E, R):
    global cnt
    
    visited[R] = cnt
    q.append(R)

    while q:
        u = q.popleft()
        for v in E[u]:
            if visited[v] == 0:
                cnt += 1
                visited[v] = cnt
                q.append(v)



# N: 정점 수, M: 간선 수, R: 시작 정점
N, M, R = map(int, input().split())

# E: 간선 정보
E = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

# 간선 오름차순 정렬
for edge in E:
    edge.sort(reverse=True)

# visited: 방문 기록용 리스트, cnt: 방문 순서
visited = [0 for _ in range(N + 1)]
q = deque()
cnt = 1

bfs(N, E, R)

for i in range(1, N + 1):
    print(visited[i])
