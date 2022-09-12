# 220912 1707 이분 그래프

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline


# bfs 함수 선언
def bfs(start):

    queue = deque()
    visited[start] = 1
    # 방문 표시를 함께 큐에 저장
    queue.append((start, 1))

    while queue:
        start, mark = queue.popleft()
        # visited 부호를 바꿔가면서 탐색
        for node in graph[start]:
            if visited[node] == 0:
                visited[node] = -mark
                queue.append((node, -mark))


# 이분 그래프 판별 함수 선언
def is_bipartite(visited):
    # 인접 리스트 내에 visited 부호가 같은 노드 존재 시 이분 그래프 x
    for i in range(1, V + 1):
        for adj in graph[i]:
            if visited[i] == visited[adj]:
                print('NO')
                return

    # 검증 통과 시 이분 그래프 o
    print('YES')
    return


# K: 테스트 케이스 개수
K = int(input())

for _ in range(K):

    # V: 정점의 개수, E: 간선의 개수 
    V, E = map(int, input().split())

    # 그래프 만들기
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        node_1, node_2 = map(int, input().split())
        graph[node_1].append(node_2) 
        graph[node_2].append(node_1) 

    # visited: 방문 여부 표시 배열
    visited = [0 for _ in range(V + 1)]

    # 미방문 노드에서 bfs
    for i in range(1, V + 1):
        if visited[i] == 0:
            bfs(i)
    
    # 이분 그래프 여부 출력
    is_bipartite(visited)
