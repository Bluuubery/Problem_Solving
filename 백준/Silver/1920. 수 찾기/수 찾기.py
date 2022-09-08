# 220908 1920 수 찾기

# 정답코드

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

def binary_search(target_num, left, right):
    if left > right:
        print(0)
        return

    mid = (left + right) // 2
    if target_num == numbers[mid]:
        print(1)
        return
    elif target_num > numbers[mid]:
        return binary_search(target_num, mid + 1, right)
    else:
        return binary_search(target_num, left, mid - 1)

numbers.sort()

for target_num in targets:
    binary_search(target_num, 0, N - 1)