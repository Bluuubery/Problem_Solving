import heapq
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221002 4485 녹색 옷 입은 애가 젤다지?

# 정답코드

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(r, c):
    queue = []

    heapq.heappush(queue, (arr[r][c], r, c))

    total_cost[r][c] = arr[r][c]

    while queue:
        weight, r, c = heapq.heappop(queue)

        if total_cost[r][c] == weight:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    cost = total_cost[r][c] + arr[nr][nc]

                    if cost < total_cost[nr][nc]:
                        total_cost[nr][nc] = cost
                        heapq.heappush(queue, (cost, nr, nc))
                
    return


tc = 1
while True:
    N = int(input())

    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]

    total_cost = [[float('inf') for _ in range(N)] for _ in range(N)]

    dijkstra(0, 0)
    print(f'Problem {tc}: {total_cost[N - 1][N - 1]}')
    
    tc += 1
