# 220915 15650 N과 M(2)

# 정답코드

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# sequence: 수열을 담을 배열 (0으로 초기화)
sequence = []


def back_tracking(current):

    if len(sequence) == M:
        print(*sequence)
        return

    for i in range(current, N + 1):
        if i not in sequence:
            sequence.append(i)

            back_tracking(i + 1)
            sequence.pop()


back_tracking(1)