import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220927 1753 최단경로

# 정답코드


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))

    distance[start] = 0

    while queue:
        weight, node = heapq.heappop(queue)

        if distance[node] == weight:
            for next in graph[node]:
                weight = distance[node] + next[1]

                if weight < distance[next[0]]:
                    distance[next[0]] = weight
                    heapq.heappush(queue, (weight, next[0]))
    
    return

V, E = map(int, input().split())
start = int(input())
distance = [sys.maxsize for _ in range(V + 1)]

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((node2, weight))

dijkstra(start)
# print(distance)

for i in range(1, V + 1):
    if distance[i] == sys.maxsize:
        print('INF')
    else:
        print(distance[i])
