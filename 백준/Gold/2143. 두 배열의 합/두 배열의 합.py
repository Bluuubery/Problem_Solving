# 220914 2143 두 배열의 합

# 정답코드

from bisect import bisect_left, bisect_right
from itertools import combinations
import sys
input = sys.stdin.readline

# T: 부 배열의 합으로 만들고자 하는 수
T = int(input())

# N: 배열 a의 크기, numbers_a: 배열 a
N = int(input())
numbers_a = list(map(int, input().split()))

# M: 배열 b의 크기, numbers_b: 배열 b
M = int(input())
numbers_b = list(map(int, input().split()))


# 누적합 구하는 함수
def cumulatinve_sum(arr):

    result = [0]
    for i in range(len(arr)):
        result.append(arr[i] + result[-1])
    
    return result


# 모든 부분합 구하는 함수
def prefix_sum(sum_list):

    result = []
    # 누적합의 두 원소를 빼서 구간합을 구한다.
    for i, j in combinations(range(len(sum_list)), 2):
        result.append(sum_list[j] - sum_list[i])

    return result


# 배열 a의 구간합
prefix_a = prefix_sum(cumulatinve_sum(numbers_a))

# 배열 b의 구간합
prefix_b = prefix_sum(cumulatinve_sum(numbers_b))
# 이분탐색하기 위해서 정렬
prefix_b.sort()

# 찾고자 하는 수가 있는지 확인하기 위한 셋
prefix_b_set = set(prefix_b)

# cnt 부 배열 쌍의 개수
cnt = 0
for num in prefix_a:
    target = T - num
    # a의 구간합에 대해 합이 T가 되도록 하는 b의 구간합이 존재
    if target in prefix_b_set:
        # 해당 구간합의 개수 더해주기
        cnt += bisect_right(prefix_b, target) - bisect_left(prefix_b, target)

# 정답 출력
print(cnt)