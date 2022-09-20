import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220920 9251 LCS

# 정답코드

# str_1: 첫번째 문자열, N: 첫번째 문자열의 길이
str_1 = input()
N = len(str_1)

# str_2: 두번째 문자열, M: 두번째 문자열의 길이
str_2 = input()
M = len(str_2)

# lcs: dp 테이블 (0으로 초기화)
lcs = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        # 문자열 내에서 두 문자가 같을 떄 lcs의 길이는 직전 lcs의 길이 + 1이다.
        if str_1[i] == str_2[j]:
            lcs[i + 1][j + 1] = lcs[i][j] + 1
        # 다를 경우 lcs의 길이는 두 직전(-1) lcs 중 최장길이 lsc이다.
        else:
            lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])

# 최종 lcs의 길이 출력
print(lcs[-1][-1])
