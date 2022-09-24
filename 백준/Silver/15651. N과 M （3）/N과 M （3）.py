# 220915 15650 N과 M(3)

# 정답코드

import sys
input = sys.stdin.readline

# N: 수열의 범위, M: 수열의 길이
N, M = map(int, input().split())

# sequence: 수열을 담을 배열
sequence = []


# 백트래킹 함수 구현
def back_tracking():

    # 수열의 길이가 M에 도달했을 때 출력 후 재귀 탈출
    if len(sequence) == M:
        print(*sequence)
        return

    # 1 ~ N까지 자연수에 대해 탐색
    for i in range(1, N + 1):
        # 탐색 중인 수 수열에 삽입
        sequence.append(i)

        # 탈출 조건까지 재귀적으로 반복
        back_tracking()

        # 백트래킹 위해 수열에서 수 빼주기
        sequence.pop()


# 백트래킹으로 수열 출력
back_tracking()