from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220918 13913 숨바꼭질 4

# 정답코드

# N: 수빈이의 위치, K: 동생의 위치
N, K = map(int, input().split())

# visited: 방문여부 표시 배열
visited = [-1 for _ in range(100_001)]

# bfs 함수 선언
def bfs(s, e):
    queue = deque()
    queue.append((s, f'{s}'))

    visited[s] = 0


    while queue:
        v, route = queue.popleft()

        if v == e:
            print(visited[v])
            print(route)
            return



            
        for w in (v * 2, v - 1, v + 1):
            if 0 <= w < 100_001:
                if visited[w] == -1:
                    visited[w] = visited[v] + 1
                    queue.append((w, route + f' {w}'))

    return


# bfs 탐색 실시
bfs(N, K)
# print(result)
