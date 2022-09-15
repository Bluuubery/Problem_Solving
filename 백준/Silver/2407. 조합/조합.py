# 220916 2407 조합

# 정답코드

import sys
sys.stdin.readline

N, M = map(int, input().split())

ans = 1
for i in range(M):
    ans *= N - i
    ans //= i + 1


print(ans)