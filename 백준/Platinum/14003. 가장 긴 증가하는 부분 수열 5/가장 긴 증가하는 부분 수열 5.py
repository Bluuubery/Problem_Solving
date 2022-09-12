# 220912 14003 가장 긴 증가하는 부분 수열 5

# 정답코드

import sys
sys = sys.stdin.readline

# 220912 12015 가장 긴 증가하는 부분 수열 2

# 정답코드

from bisect import bisect_left
import sys
input = sys.stdin.readline

# N: 수열의 길이, numbers: 수열
N = int(input())
numbers = list(map(int, input().split()))

# lis_temp: 임시 lis
# lis_idx: 각 수의 lis에서의 idx를 담을 리스트
lis_temp = []
lis_idx = []

# 이분탐색을 통해 수열의 수가 lis에 들어갈 위치를 찾는다.
for i in range(N):
    # idx: 수가 들어갈 위치
    idx = bisect_left(lis_temp, numbers[i])
    lis_idx.append(idx)
    # 현재 lis의 길이보다 뒤쪽이면 임시 lis에 추가해준다.
    if len(lis_temp) <= idx:
        lis_temp.append(numbers[i])
    # 들어갈 위치에 있는 수와 대체
    else:
        lis_temp[idx] = numbers[i]

# lis_idx에 저장해둔 인덱스를 거꾸로 탐색해서 lis를 채워나간다.
max_idx = max(lis_idx)
lis = []
for i in range(N - 1, -1, -1):
    if lis_idx[i] == max_idx:
        lis.append(numbers[i])
        max_idx -= 1

# 거꾸로된 lis를 다시 정방향으로 뒤집어준다.
lis.reverse()

# lis의 길이, lis 출력
print(len(lis))
print(*lis)