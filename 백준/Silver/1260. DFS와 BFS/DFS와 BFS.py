# 220812 1260 DFS와 BFS

# 정답코드


from collections import deque
import sys

# 최대 재귀 깊이 제한 조정
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# dfs 함수 선언
def dfs(N, E, R):

    # 방문 순서 표시
    visited[R] = 1

    print(R, end=' ')

    # 미방문 인접 노드 깊이 순으로 방문
    for x in E[R]:
        if visited[x] == 0:
            dfs(N, E, x)


# bfs 함수 선언
def bfs(V, E, R):
    
    # 방문 표시 후 큐에 삽입
    visited[R] = 1
    q.append(R)

    print(R, end=' ')

    # 큐가 빌 때까지
    while q:
        # 큐에서 꺼낸 곳부터
        u = q.popleft()
        # 미방문 인접노드 탐색
        for v in E[u]:
            if visited[v] == 0:
                visited[v] = 1
                q.append(v)

                print(v, end=' ')



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

# visited: 방문 기록용 리스트, q: bfs 경로 저장용
visited = [0 for _ in range(N + 1)]
q = deque()

# dfs, bfs 탐색 실시
dfs(N, E, R)
print()

visited = [0 for _ in range(N + 1)]
bfs(N, E, R)