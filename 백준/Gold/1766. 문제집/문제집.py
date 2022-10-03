import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221003 1766 문제집

# 정답코드

N, M = map(int, input().split())

indegree = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    indegree[node2] += 1

result = []
queue = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    current = heapq.heappop(queue)
    result.append(current)

    for next in graph[current]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(queue, next)

print(*result)