# 220915 9663 N-Queen

# 정답코드

import sys
input = sys.stdin.readline

# N: 놓을 퀸의 개수
N = int(input())

# 열, 대각선1, 대각선2 방문 여부 표시 배열
visited_col = [0 for _ in range(N)]
visited_diagonal_1 = [0 for _ in range(2 * N)]
visited_diagonal_2 = [0 for _ in range(2 * N)]

# cnt: N-Queen를 만족하는 경우의 수 개수
cnt = 0


# 백트래킹으로 n-queen 구하는 함수 선언
# row: 퀸을 놓을 행
def n_queen(row, N):
    global cnt

    # 퀸을 다 놓았을 경우
    if row == N:
        # cnt를 세준다.
        cnt += 1
        return

    # 각 열에 대해서 퀸을 놓을 수 있는지 검증
    for col in range(N):

        # 놓고자 하는 위치의 열, 대각선 2개가 미방문상태인 경우 퀸을 놓는다.
        if visited_col[col] == 0 and visited_diagonal_1[row + col] == 0 and visited_diagonal_2[row - col + N] == 0:

            # 해당 위치의 열, 대각선 2개 방문 처리
            visited_col[col] = 1
            visited_diagonal_1[row + col] = 1
            visited_diagonal_2[row - col + N] = 1   

            # 다음 행에 대해서 탐색 진행
            n_queen(row + 1, N)

            # 백트래킹을 위해 방문 여부 초기화
            visited_col[col] = 0
            visited_diagonal_1[row + col] = 0
            visited_diagonal_2[row - col + N] = 0  


# 0번째 행부터 N 개의 퀸을 놓는다.
n_queen(0, N)

# 정답 출력
print(cnt)
