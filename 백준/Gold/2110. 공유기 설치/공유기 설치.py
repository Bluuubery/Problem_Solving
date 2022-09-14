# 220914 2110 공유기 설치

# 정답코드

import sys
input = sys.stdin.readline

N, C = map(int, input().split())

house = []
for _ in range(N):
    house.append(int(input()))

house.sort()


def parametric_search(start, end):


    if start > end:
        print(start)
        return 

    mid = (start + end) // 2

    cnt = 1
    current = house[0]
    for i in range(1, N):
        if house[i] > current + mid:
            cnt += 1
            current = house[i]

    if cnt >= C:
        parametric_search(mid + 1, end)
    else:
        parametric_search(start, mid - 1)


parametric_search(1, house[-1] - house[0])