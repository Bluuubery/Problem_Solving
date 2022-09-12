# 220912 12015 가장 긴 증가하는 부분 수열 2

# 정답코드

from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

lis = []

for i in range(N):
    idx = bisect_left(lis, numbers[i])
    if len(lis) <= idx:
        lis.append(numbers[i])
    else:
        lis[idx] = numbers[i]

print(len(lis))