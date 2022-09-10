# 220910 2295 세 수의 합

# 정답코드 (셋)

import sys
input = sys.stdin.readline

# N: 수의 개수, numbers: 수열
N = int(input())
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

# two_sum_set: numbers 리스트의 두 원소의 합을 담은 셋
two_sum_set = set()

for i in range(N):
    for j in range(N):
        two_sum_set.add(numbers[i] + numbers[j])


# 최댓값을 찾아야 하므로 numbers는 내림차순으로 정렬
numbers.sort(reverse=True)

# target: 찾고자 하는 수
# 셋 통해서 target - numbers[j]가 two_sum_set에 존재하는지 확인한다.
for i in range(N):
    target = numbers[i]
    for j in range(N):
        if target - numbers[j] in two_sum_set:
            print(target)
            exit(0)