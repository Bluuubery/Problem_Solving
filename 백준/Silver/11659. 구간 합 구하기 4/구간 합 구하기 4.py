# 220818 11659 구간 합 구하기 4

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

# 누적합 리스트를 먼저 만들어 둔다.(시간복잡도 O(N))
sum_numbers= [0, numbers[0]]
for i in range(1, N):
    sum_numbers.append(numbers[i] + sum_numbers[-1])

# 인덱스를 통해 바로 접근한다. (시간복잡도 O(1))
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_numbers[j] - sum_numbers[i - 1])