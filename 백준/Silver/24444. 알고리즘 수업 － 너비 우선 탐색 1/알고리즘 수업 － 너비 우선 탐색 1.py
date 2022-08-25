# 220825 24444 알고리즘 수업 - 너비 우선 탐색 1

from collections import deque
import sys

input = sys.stdin.readline


# bfs 함수 선언
def bfs(V, E, R):
    global cnt
    
    # 방문 표시 후 큐에 삽입
    visited[R] = cnt
    q.append(R)

    # 큐가 빌 때까지
    while q:
        # 큐에서 꺼낸 곳부터
        u = q.popleft()
        # 미방문 인접노드 탐색
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
    edge.sort()

# visited: 방문 기록용 리스트, q: bfs 경로 저장용, cnt: 방문 순서
visited = [0 for _ in range(N + 1)]
q = deque()
cnt = 1

# bfs 탐색 실시
bfs(N, E, R)

# 방문 순서 출력
for i in range(1, N + 1):
    print(visited[i])
