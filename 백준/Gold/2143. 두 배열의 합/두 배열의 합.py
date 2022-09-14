# 220914 2143 두 배열의 합

# 정답코드

from bisect import bisect_left, bisect_right
from itertools import combinations
import sys
input = sys.stdin.readline

T = int(input())

N = int(input())
numbers_a = list(map(int, input().split()))

M = int(input())
numbers_b = list(map(int, input().split()))


def cumulatinve_sum(arr):

    result = [0]
    for i in range(len(arr)):
        result.append(arr[i] + result[-1])
    
    return result


def prefix_sum(sum_list):

    result = []
    for i, j in combinations(range(len(sum_list)), 2):
        result.append(sum_list[j] - sum_list[i])
    # print(result)
    return result


prefix_a = prefix_sum(cumulatinve_sum(numbers_a))
prefix_a.sort()

prefix_b = prefix_sum(cumulatinve_sum(numbers_b))
prefix_b.sort()

prefix_b_set = set(prefix_b)

cnt = 0
for num in prefix_a:
    target = T - num
    if target in prefix_b_set:
        cnt += bisect_right(prefix_b, target) - bisect_left(prefix_b, target)


print(cnt)