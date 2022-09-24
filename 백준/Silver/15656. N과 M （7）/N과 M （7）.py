# 220915 15656 N과 M (7)

# 정답코드

import sys
input = sys.stdin.readline

# N: 수열의 범위, M: 수열의 길이, numbers: 탐색할 수열
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

# sequence: 결과 수열을 담을 배열
sequence = []


# 백트래킹 함수 구현
def back_tracking():

    # 수열의 길이가 M에 도달했을 때 출력 후 재귀 탈출
    if len(sequence) == M:
        print(*sequence)
        return

    # 중복 선택 가능하므로 수열 전체를 범위로 지정
    for i in range(N):
        # 선택한 수 수열에 삽입
        sequence.append(numbers[i])

        # 재귀적으로 반복
        back_tracking()

        # 백트래킹 위해 수열에서 수 빼주기
        sequence.pop()


# 백트래킹으로 수열 출력
back_tracking()