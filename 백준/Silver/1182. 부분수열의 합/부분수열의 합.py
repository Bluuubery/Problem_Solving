# 220915 1182 부분수열의 합

# 정답코드

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

subsequence = []
cnt = 0

def backtracking(current, N, S, K):

    global cnt

    if S >= 0:
        if sum(subsequence) > S:
            return

    if len(subsequence) == K:
        if sum(subsequence) == S:
            cnt += 1
            return

    for i in range(current, N):
        subsequence.append(numbers[i])

        backtracking(i + 1, N, S, K)

        subsequence.pop()

for i in range(1, N + 1):
    backtracking(0, N, S, i)

print(cnt)