# 220914 2110 공유기 설치

# 정답코드

import sys
input = sys.stdin.readline

# N: 집의 개수, C: 설치하고자 하는 공유기의 개수
N, C = map(int, input().split())

# house: 집의 위치 정보
house = []
for _ in range(N):
    house.append(int(input()))

# 이분탐색 위해서 정렬
house.sort()


# 매개변수 탐색
def parametric_search(start, end):

    # 탐색 종료 조건
    if start > end:
        print(start)
        return 

    # mid: 공유기 간 최소 거리
    mid = (start + end) // 2

    # cnt: 설치한 공유기의 대수, current: 현재 공유기를 설치한 집 번호(첫 집에 설치로 초기화)
    cnt = 1
    current = house[0]
    # 현재 탐색하고 있는 거리와 같거나 그보다 멀리 설치
    for i in range(1, N):
        if house[i] > current + mid:
            cnt += 1
            current = house[i]

    # 현재 설치한 공유기가 설치하고자 하는 공유기보다 많거나 같은 경우
    if cnt >= C:
        # 간격을 넓혀서 설치 탐색
        parametric_search(mid + 1, end)
    # 현재 설치한 공유기가 설치하고자 하는 공유기보다 적은 경우
    else:
        # 간격을 좁혀서 설치 탐색
        parametric_search(start, mid - 1)


# 1을 최소 간격, 끝집과 첫집 간의 간격을 최대 간격으로 설정하고 탐색 시작
parametric_search(1, house[-1] - house[0])