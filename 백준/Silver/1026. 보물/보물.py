# 220904 보물 1026

# 정답코드

import sys
input = sys.stdin.readline

# N: 각 수열의 원소의 개수, A, B: 수열 
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A와 B를 서로 역순으로 정렬한다.
A.sort()
B.sort(reverse=True)

# ans: 결과값을 담을 변수
ans = 0
# A와 B의 원소를 각각 곱해서 결괏값에 더해준다.
for i in range(N):
    ans += A[i] * B[i]

print(ans)