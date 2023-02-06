import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

# 220809 10989 수정렬하기3

N = int(input())

arr = [0] * 10001

for _ in range(N):
    arr[int(input())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)