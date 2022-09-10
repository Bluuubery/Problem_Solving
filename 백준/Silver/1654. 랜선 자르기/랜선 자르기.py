# 220910 1654 랜선자르기

# 정답코드

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lan = []
for _ in range(N):
    lan.append(int(input()))


def binary_search(arr, start, end):
    if start > end:
        print(end)
        return 

    mid = (start + end) // 2

    cnt = 0
    for i in range(N):
        cnt += lan[i] // mid
    
    if cnt >= K:
        binary_search(arr, mid + 1, end)
    else:
        binary_search(arr, start, mid - 1)
    
binary_search(lan, 1, max(lan))