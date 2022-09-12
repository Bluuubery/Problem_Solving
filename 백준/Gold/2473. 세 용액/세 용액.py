# 220912 2473 세 용액

# 정답코드

import sys
input = sys.stdin.readline

# N: 용액의 수, liquid: 용액들의 특성값
N = int(input())
liquid = list(map(int, input().split()))

# 이분탐색을 위해 정렬
liquid.sort()

# min_sum: 최소 특성값의 핪
min_sum = sys.maxsize

# 두 용액 합을 구하고 합이 0이 되도록 하는 세번째 용액을 이분탐색으로 찾기
for i in range(N- 1):
    for j in range(i + 1, N):
        target = liquid[i] + liquid[j]

        start = j + 1
        end = N - 1

        while start <= end:
            mid = (start + end) // 2

            # 합이 0이면 정답 출력하고 즉시 종료
            if target + liquid[mid] == 0:
                print(liquid[i], liquid[j], liquid[mid])
                exit(0)
            
            elif target + liquid[mid] > 0:
                end = mid - 1
            
            else:
                start = mid + 1
            
            # 최솟값 비교해가면서 갱신
            if abs(target + liquid[mid]) < abs(min_sum):
                min_sum = target + liquid[mid]
                min_liquids = [liquid[i], liquid[j], liquid[mid]]

# 최솟값이 되도록 하는 세 용액 출력
print(*min_liquids)
