import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221002 1238 파티

# 정답코드


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        weight, node = heapq.heappop(queue)

        if distance[node] == weight:
            for next in graph[node]:
                dist = distance[node] + next[1]

                if dist < distance[next[0]]:
                    distance[next[0]] = dist
                    heapq.heappush(queue, (dist, next[0]))

    return distance



N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((node2, weight))

result = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    distance = [float('inf') for _ in range(N + 1)]
    result[i] = dijkstra(i)[X]


distance = [float('inf') for _ in range(N + 1)]
for i in range(1, N + 1):
    result[i] += dijkstra(X)[i]

print(max(result[1:]))