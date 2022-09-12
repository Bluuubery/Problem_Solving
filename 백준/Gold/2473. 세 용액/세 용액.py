# 220912 2473 세 용액

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

min_sum = sys.maxsize

for i in range(N- 1):
    for j in range(i + 1, N):
        target = liquid[i] + liquid[j]

        start = j + 1
        end = N - 1

        while start <= end:
            mid = (start + end) // 2

            if target + liquid[mid] == 0:
                print(liquid[i], liquid[j], liquid[mid])
                exit(0)
            
            elif target + liquid[mid] > 0:
                end = mid - 1
            
            else:
                start = mid + 1
            
            if abs(target + liquid[mid]) < abs(min_sum):
                min_sum = target + liquid[mid]
                min_liquids = [liquid[i], liquid[j], liquid[mid]]

print(*min_liquids)
