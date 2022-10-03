from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221003 2252 줄 세우기

# 정답코드

# N: 정점 개수, M: 간선 개수
N, M = map(int, input().split())

# N: 각 노드별 진입 차수 저장 리스트
indegree = [0 for _ in range(N + 1)]

# graph: 인접리스트로 구현한 그래프
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    # 간선 정보를 저장해주고 진입 차수를 기록해준다.
    graph[node1].append(node2)
    indegree[node2] += 1

# queue: 위상 정렬 시 사용할 큐, result: 정렬된 결과값을 담을 리스트
queue = deque()
result = []

# 진입 차수가 0인 정점을 큐에 담아준다
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 큐가 빌 떄까지 위상정렬 수행
while queue:
    # 진입 차수가 0인 정점을 result에 담아준다.
    current = queue.popleft()
    result.append(current)

    # 인접한 정점의 진입 차수를 1씩 뺴준다.
    for next in graph[current]:
        indegree[next] -= 1

        # 인접 정점의 진입차수가 0이 되었을 경우 큐에 담아준다.
        if indegree[next] == 0: 
            queue.append(next)

    
# 정렬된 결과 출력
print(*result)