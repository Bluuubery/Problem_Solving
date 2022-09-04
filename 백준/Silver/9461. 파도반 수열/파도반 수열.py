# 220904 9461 파도반 수열

# 정답 코드

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    P = [0, 1, 1, 1, 2, 2]

    if N <= 5:
        print(P[N])
    else:
        for i in range(6, N + 1):
            P.append(P[i - 1] + P[i - 5])
        
        print(P[N])
