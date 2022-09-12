# 220912 12015 가장 긴 증가하는 부분 수열 2

# 정답코드

from bisect import bisect_left
import sys
input = sys.stdin.readline

# N: 수열의 길이, numbers: 수열
N = int(input())
numbers = list(map(int, input().split()))

# lis: lis
lis = []

# 이분탐색을 통해 수열의 수가 lis에 들어갈 위치를 찾는다.
for i in range(N):
    # idx: 수가 들어갈 위치
    idx = bisect_left(lis, numbers[i])
    # 현재 lis의 길이보다 뒤쪽이면 lis에 추가해준다.
    if len(lis) <= idx:
        lis.append(numbers[i])
    # 들어갈 위치에 있는 수와 대체
    else:
        lis[idx] = numbers[i]

print(len(lis))