# 220915 9663 N-Queen

# 정답코드

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
# 체스판
board = [[0 for _ in range(N)] for _ in range(N)]

# 열, 대각선1, 대각선2
visited_col = [0 for _ in range(N)]
visited_diagonal_1 = [0 for _ in range(2 * N)]
visited_diagonal_2 = [0 for _ in range(2 * N)]

# 엔퀸 개수
cnt = 0


def n_queen(row, N):
    global cnt

    # 깊이 도달 시 
    if row == N:
        cnt += 1
        return

    for col in range(N):
        # 미방문
        if visited_col[col] == 0 and visited_diagonal_1[row + col] == 0 and visited_diagonal_2[row - col + N] == 0:

            # 방문처리
            visited_col[col] = 1
            visited_diagonal_1[row + col] = 1
            visited_diagonal_2[row - col + N] = 1   

            n_queen(row + 1, N)

            # 백트래킹
            visited_col[col] = 0
            visited_diagonal_1[row + col] = 0
            visited_diagonal_2[row - col + N] = 0  


n_queen(0, N)

print(cnt)