import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220920 9251 LCS

# 정답코드

str_1 = input()
N = len(str_1)

str_2 = input()
M = len(str_2)

lcs = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        if str_1[i] == str_2[j]:
            lcs[i + 1][j + 1] = lcs[i][j] + 1
        else:
            lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])

print(lcs[-1][-1])
