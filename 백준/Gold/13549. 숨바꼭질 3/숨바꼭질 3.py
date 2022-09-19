from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220918 13549 숨바꼭질3

# 정답코드

# N: 수빈이의 위치, K: 동생의 위치
N, K = map(int, input().split())

# visited: 방문여부 표시 배열
visited = [0 for _ in range(200_001)]


def bfs(s, e, t):
    queue = deque()
    queue.append((s, t))
    ans = sys.maxsize

    while queue:
        v, t = queue.popleft()

        if v == e:
            print(visited[v])
            return
            # ans = min(ans, t)
        
        for w in (v * 2, v - 1, v + 1):
            if 0 <= w < 200_001 and visited[w] == 0:
                if w == v * 2:
                    visited[w] = visited[v]
                    queue.append((w, t))
                else:
                    visited[w] = visited[v] + 1
                    queue.append((w, t + 1))

    # print(ans)
    return

bfs(N, K, 0)
