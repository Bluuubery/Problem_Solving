# 230117 삼각형 만들기

# 정답코드

N = int(input())

ans = 0

for i in range(1, N):
    for j in range(i, N):
        k = N - (i + j)
        if i + j > k and k >= j:
            ans += 1

print(ans)