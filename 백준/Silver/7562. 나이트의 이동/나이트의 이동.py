# 220826 7562 나이트의 이동

from collections import deque
import sys

input = sys.stdin.readline

# 나이트 이동 범위 설정
dr = [2, 1, -1, -2, -2, -1, 1, 2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]


# bfs 함수 선언
def bfs(r, c):
    q = deque()
    q.append((r, c))

    # 방문 표시
    chess[r][c] = 1

    while q:
        r, c = q.popleft()

        for i in range(8):
            n_r = r + dr[i]
            n_c = c + dc[i]
            
            # 목표 지점에 도착하면 이동 횟수 출력 후 중단
            if (n_r, n_c) == (e_r, e_c):
                print(chess[r][c])
                return
            
            elif 0 <= n_r < L and 0 <= n_c < L:
                if chess[n_r][n_c] == 0:
                    chess[n_r][n_c] = chess[r][c] + 1
                    q.append((n_r, n_c))



T = int(input())
for _ in range(T):
    # L: 체스판의 길이, s_r, s_c: 나이트 현재 위치, e_r, e_c: 나이트 목표 위치
    L = int(input())
    s_r, s_c = map(int, input().split())
    e_r, e_c = map(int, input().split())

    # chess: 체스판
    chess = [[0 for _ in range(L)] for _ in range(L)]

    # 출발 위치가 목표 위치인 경우 바로 0 출력
    if (s_r, s_c) == (e_r, e_c):
        print(0)
    # bfs 탐색 실시
    else:
        bfs(s_r, s_c)
