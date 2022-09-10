# 220910 2295 세 수의 합

# 정답코드 (딕셔너리)

from collections import defaultdict
import sys
input = sys.stdin.readline

# N: 수의 개수, numbers: 수열
N = int(input())
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

# two_sum: numbers 리스트의 두 원소의 합들을 담은 배열
two_sum = []
two_sum_dict = defaultdict(int)

for i in range(N):
    for j in range(N):
        sum_num = numbers[i] + numbers[j]
        two_sum.append(sum_num)
        two_sum_dict[sum_num] += 1

# 두 리스트를 정렬해준다.
two_sum.sort()
# 최댓값을 찾아야 하므로 numbers는 내림차순으로 정렬
numbers.sort(reverse=True)

# target: 찾고자 하는 수
for i in range(N):
    target = numbers[i]
    for j in range(N):
        if two_sum_dict[target - numbers[j]]:
            print(target)
            exit(0)