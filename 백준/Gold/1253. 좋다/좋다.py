# 220907 1253 좋다

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

good = 0
for i in range(N):
    target = numbers.pop(i)
    start = 0
    end = N - 2
    while end > start:
        if numbers[start] + numbers[end] == target:
            good += 1
            break
        elif numbers[start] + numbers[end] > target:
            end -= 1
        else:
            start += 1
    numbers.insert(i, target)

print(good)