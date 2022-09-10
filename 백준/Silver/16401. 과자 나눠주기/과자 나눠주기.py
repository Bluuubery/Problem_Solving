# 220910 16401 과자 나눠주기

# 정답코드

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
cookie = list(map(int, input().split()))

cookie.sort()


def parametric_search(arr, start, end):
    if start > end:
        print(end)
        return
    
    mid = (start + end) // 2

    if mid == 0:
        print(0)
        return

    cnt = 0
    for i in range(N):
        cnt += cookie[i] // mid
    
    if cnt >= M:
        parametric_search(arr, mid + 1, end)
    else:
        parametric_search(arr, start, mid - 1)


parametric_search(cookie, 0, cookie[-1])