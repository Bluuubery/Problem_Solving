import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221002 1261 알고스팟

# 정답코드


def dijkstra(r, c):
    queue = []
    heapq.heappush(queue, (0, r, c))
    distance[r][c] = 0

    while queue:
        weight, r, c = heapq.heappop(queue)

        if distance[r][c] == weight:
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < M and 0 <= nc < N:
                    if arr[nr][nc] + weight < distance[nr][nc]:
                        distance[nr][nc] = arr[nr][nc] + weight
                        heapq.heappush(queue, (arr[nr][nc] + weight, nr, nc))
    
    print(distance[M - 1][N - 1])
    return
 

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]

distance = [[float('INF') for _ in range(N)] for _ in range(M)]

dijkstra(0, 0)