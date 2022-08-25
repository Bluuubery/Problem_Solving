# 220812
# 24479 알고리즘 수업 - 깊이 우선 탐색 1

# 정답코드

import sys
# 최대 재귀 깊이 제한 조정
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# dfs 함수 선언
def dfs(N, E, R):
    # 글로벌 변수 선언
    global visited
    global cnt

    # 방문 순서 표시
    visited[R] = cnt

    # 미방문 인접 노드 깊이 순으로 방문
    for x in E[R]:
        if visited[x] == 0:
            cnt += 1
            dfs(N, E, x)


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

# visited: 방문 기록용 리스트, cnt: 방문 순서
visited = [0 for _ in range(N + 1)]
cnt = 1

# dfs 탐색 실시
dfs(N, E, R)

# 방문 순서 출력
for i in range (1, N + 1):
    print(visited[i])

    