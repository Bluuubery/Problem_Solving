# 220913 1240 노드사이의 거리

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

# N: 노드의 개수, M: 거리를 구할 노드 쌍
N, M = map(int, input().split())

# tree: 인접 리스트로 구현한 트리
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node_1, node_2, weight = map(int, input().split())
    tree[node_1].append([node_2, weight])
    tree[node_2].append([node_1, weight])


# bfs 함수 선언
def bfs(start, end):
    visited[start] = 0

    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        # 목표 노드에 도착하면 거리 출력 후 반환
        if node == end:
            print(visited[node])
            return

        # 미방문 노드에 거리 더해가면서 탐색
        for next, weight in tree[node]:
            if visited[next] == -1:
                visited[next] = visited[node] + weight
                queue.append(next)

    # 목표 노드 거리 출력 후 반환
    print(visited[node])
    return


for _ in range(M):
    start, end = map(int, input().split())

    # visited: 방문 여부 표시 배열 -1로 초기화
    visited = [-1 for _ in range(N + 1)]
    
    # 입력 받은 출발점과 도착점으로 bfs 탐색
    bfs(start, end)