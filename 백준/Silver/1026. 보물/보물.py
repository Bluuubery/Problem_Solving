# 220904 보물 1026

# 정답코드

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

ans = 0
for i in range(N):
    ans += A[i] * B[i]

print(ans)