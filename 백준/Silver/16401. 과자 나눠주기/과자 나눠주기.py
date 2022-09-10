# 220910 16401 과자 나눠주기

# 정답코드

import sys
input = sys.stdin.readline

# M: 조카의 수, N: 과자의 수, cookie: 과자의 길이
M, N = map(int, input().split())
cookie = list(map(int, input().split()))

cookie.sort()


# 파라매틱 서치 함수 선언
def parametric_search(arr, start, end):
    # 정답 출력 후 반환
    if start > end:
        print(end)
        return
    
    mid = (start + end) // 2

    # 나눠주지 못할 경우 0 출력 후 반환
    if mid == 0:
        print(0)
        return

    # cnt: 해당 길이로 나눠줄 때 나눠줄 수 있는 조카 수
    cnt = 0
    for i in range(N):
        cnt += cookie[i] // mid
    
    if cnt >= M:
        parametric_search(arr, mid + 1, end)
    else:
        parametric_search(arr, start, mid - 1)


# 파라매틱 서치
parametric_search(cookie, 0, cookie[-1])