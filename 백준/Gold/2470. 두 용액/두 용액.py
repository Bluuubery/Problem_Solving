# 220911 2470 두 용액

# 정답코드

import sys
import bisect
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

min_sum = sys.maxsize

for i in range(N - 1):
    start = i + 1
    end = N - 1
    while start <= end:

        mid = (start + end) // 2

        if liquid[i] + liquid[mid] == 0:
            print(liquid[i], liquid[mid])
            exit(0)
        elif liquid[i] + liquid[mid] > 0:
            end = mid - 1
        else:
            start = mid + 1
    
        if abs(liquid[i] + liquid[mid]) < abs(min_sum):
            min_sum = liquid[i] + liquid[mid]
            min_pair = [liquid[i], liquid[mid]]


print(*min_pair)