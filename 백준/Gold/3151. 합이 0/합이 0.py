# 220810 3151 합이 0 

# 정답코드

from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N = int(input())

students = list(map(int, input().split()))
students.sort()

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        target = -(students[i] + students[j])
        left = bisect_left(students, target, j + 1, N)
        right = bisect_right(students, target, j + 1, N)
        cnt += right - left

print(cnt)