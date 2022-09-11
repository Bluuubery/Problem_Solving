# 220830 3190 뱀

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

# 배열
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

# 사과
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r- 1][c- 1] = 2

# 방향전환
L = int(input())
turn = dict()
for _ in range(L):
    cnt, direction = input().split()
    turn[int(cnt)] = direction

# 탐색 방향 (처음에 우를 보고 있으므로 시계방향으로)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def snake(r, c):
    cnt = 0
    d = 0
    queue = deque()

    board[r][c] = 1
    queue.append((r, c))
    while True:
        cnt += 1



        nr = r + dr[d]
        nc = c + dc[d]

        if not 0 <= nr < N or not 0 <= nc < N:
            break

        if board[nr][nc] == 2:
            board[nr][nc] = 1
            r, c = nr, nc
            queue.append((r, c))
        
        elif board[nr][nc] == 0:
            board[nr][nc] = 1
            r, c = nr, nc
            queue.append((r, c))
            r_tail, c_tail = queue.popleft()
            board[r_tail][c_tail] = 0
        
        else:
            break
        
        if cnt in turn:
            if turn[cnt] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
    
    # for i in board:
    #     print(*i)
    print(cnt)
    return

snake(0, 0)
            
