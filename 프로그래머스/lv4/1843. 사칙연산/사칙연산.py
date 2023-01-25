import sys


def solution(arr):
    answer = -1

    N = len(arr)//2 + 1
    INF = sys.maxsize

    # dp 테이블 초기화 (범위에 따른 최솟값 최댓값 연산 테이블)
    dp_min = [[INF for _ in range(101)] for _ in range(101)]
    dp_max = [[-INF for _ in range(101)] for _ in range(101)]

    for i in range(0, N):
        dp_min[i][i] = int(arr[i * 2])
        dp_max[i][i] = int(arr[i * 2])

    # 계산 범위
    for calculate_range in range(1, N):
        # i: 시작 피연산자
        for i in range(0, N - calculate_range):
            # j: 마지막 피연산자
            j = calculate_range + i

            for k in range(i, j):

                # + 연산자
                if arr[k*2 + 1] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                # - 연산자
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])

    answer = dp_max[0][N - 1]

    return answer