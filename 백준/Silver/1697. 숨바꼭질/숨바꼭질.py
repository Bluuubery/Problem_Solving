# 220826 1697 숨바꼭질

from collections import deque
import sys

input = sys.stdin.readline


def bfs(s, e):
    q = deque()
    q.append(s)                 

    while q:                    
        v = q.popleft()

        if v == e:
            print(visited[v])
            break

        for w in (v - 1, v + 1, v * 2):    
            if 0<= w < 200_001 and visited[w] == 0:
                visited[w] = visited[v] + 1
                q.append(w)

N, K = map(int, input().split())
visited = [0 for _ in range(200_001)]

bfs(N, K)
