import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221002 9370 미확인 도착지

# 정답코드


def dijkstar(start):

    queue = []
    heapq.heappush(queue, (0, start))

    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] == dist:
            for next in graph[node]:
                dist = distance[node] + next[1]

                if dist < distance[next[0]]:
                    distance[next[0]] = dist
                    heapq.heappush(queue, (dist, next[0]))


    return



tc = int(input())

for _ in range(tc):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())


    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        node1, node2, weight = map(int, input().split())
        if (node1 == G and node2 == H) or (node1 == H and node2 == G):
            weight -= 0.1

        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))


    candidates = []
    for _ in range(T):
        candidates.append(int(input()))
        


    distance = [sys.maxsize for _ in range(N + 1)]
    dijkstar(S)

    ans = []
    for candidate in candidates:
        if type(distance[candidate]) == float:
            ans.append(candidate)
    ans.sort()
        
    print(*ans)
