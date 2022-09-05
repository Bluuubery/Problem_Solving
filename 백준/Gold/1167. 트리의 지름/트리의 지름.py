# 220905 1167 트리의 지름

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())

# tree: 트리 인접 리스트
tree = [[] for _ in range(N + 1)]
# 인덱싱을 이용해 가중치와 노드의 정보를 인접리스트 형태로 담아준다.
for _ in range(N):
    edge = list(map(int, input().split()))
    for i in range(1, len(edge) - 1, 2):
        tree[edge[0]].append([edge[i], edge[i + 1]])


# 가중치를 가진 트리에서의 dfs함수
def dfs(s):

    for edge in tree[s]:
        node = edge[0]
        weight = edge[1]
        # 가중치를 visted에 더해나가면서 탐색 실시
        if visited[node] == -1:
            visited[node] = visited[s] + weight
            dfs(node)

# visited: 방문 여부 표시 배열(-1로 초기화)
visited = [-1] * (N + 1)
# 루트에서 출발해 dfs 실시
visited[1] = 0
dfs(1)

# s: 루트에서 가장 먼 곳에 위치한 노드
s = visited.index(max(visited))
# visited 배열을 초기화해주고 노드 s를 출발점으로 dfs 실시 
visited = [-1] * (N + 1)
visited[s] = 0
dfs(s)

# 트리의 지름 출력
print(max(visited))
