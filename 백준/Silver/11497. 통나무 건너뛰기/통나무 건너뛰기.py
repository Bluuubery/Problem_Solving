# 220814 11497 통나무 건너뛰기

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    # 통나무의 높이를 입력 받아 내림차순으로 정렬한다.
    logs = list(map(int, input().split()))
    logs.sort()

    # 높이 차가 최소가 되는 배열은 역피라미드(피라미드)형 배열이다.
    # ex) 통나무 높이가 10, 9, 8, 7, 6, 5, 4, 3, 2, 1이면
    # 10 8 6 4 2 0 1 3 5 7 9

    # 통나무의 높이차를 담을 리스트
    gap = list()
    # 위와 같은 방식으로 배열 했을 때의 높이차를 계산한다.
    # 피라미드형은 절댓값으로 계산해야된다.
    gap.append(logs[1] - logs[0])
    for i in range(2, N):
        gap.append(logs[i] - logs[i - 2])

    # 최대 높이차 출력
    print(max(gap))
