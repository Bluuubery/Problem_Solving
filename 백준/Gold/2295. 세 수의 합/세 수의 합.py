# 220910 2295 세 수의 합

# 정답코드

import sys
input = sys.stdin.readline


def binary_search(target, arr, left, right):
    if left > right:
        return False
    
    mid = (left + right) // 2
    if target == arr[mid]:
        return True
    elif target > arr[mid]:
        return binary_search(target, arr, mid + 1, right)
    else:
        return binary_search(target, arr, left, mid - 1)


N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

two_sum = []

for i in range(N):
    for j in range(N):
        two_sum.append(numbers[i] + numbers[j])

two_sum.sort()
numbers.sort(reverse=True)

for i in range(N):
    target = numbers[i]
    for j in range(N):
        if binary_search(target - numbers[j], two_sum, 0, len(two_sum) - 1):
            print(target)
            exit(0)
