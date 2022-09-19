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


# bfs 함수 선언
def bfs(s, e):
    queue = deque()
    queue.append(s)

    while queue:
        v = queue.popleft()

        # 목표 지점 도착 시 시간 출력 후 반환
        if v == e:
            print(visited[v])
            return
        
        # v * 2의 시간이 0이므로 v * 2 먼저 방문
        for w in (v * 2, v - 1, v + 1):
            if 0 <= w < 200_001 and visited[w] == 0:
                # v * 2는 시간을 더해주지 않는다.
                if w == v * 2:
                    visited[w] = visited[v]
                    queue.append(w)
                # 그 외는 시간을 더해주면서 탐색한다.
                else:
                    visited[w] = visited[v] + 1
                    queue.append(w)

    return


# bfs 탐색 실시
bfs(N, K)
