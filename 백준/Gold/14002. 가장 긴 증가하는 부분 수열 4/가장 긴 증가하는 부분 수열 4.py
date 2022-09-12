# 220912 14002 가장 긴 증가하는 부분 수열 4

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

# dp: 부분수열의 길이를 담을 dp테이블
dp = []
for i in range(N):
    # 초기화
    if i == 0:
        dp.append(1)
    else:
        # 1로 초기화
        dp.append(1)
        for j in range(i):
            # 자신보다 작은 수의 부분수열에서 자신을 이어붙인 부분수열의 길이와 지속적으로 비교하면서 갱신
            if numbers[i] > numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)

# lis: 실제 부분수열을 담을 리스트
idx = max(dp)
lis = []
# 역순으로 탐색하면서 부분수열을 거꾸로 채워나간다.
for i in range(N - 1, -1, -1):
    if dp[i] == idx:
        lis.append(numbers[i])
        idx -= 1

# 거꾸로 채운 부분 수열을 다시 정방향으로 뒤집어준다.
lis.reverse()

print(max(dp))
print(*lis)