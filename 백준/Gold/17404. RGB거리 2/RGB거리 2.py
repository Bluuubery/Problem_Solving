import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221001 17404 rgb거리 2

# 정답코드

N = int(input())

rgb = [list(map(int, input().split())) for _ in range(N)]

ans = sys.maxsize
for i in range(3):
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0] = [sys.maxsize] * 3
    dp[0][i] = rgb[0][i]

    for j in range(1, N):
        dp[j][0] = rgb[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = rgb[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = rgb[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    for k in range(3):
        if i == k:
            continue
        ans = min(ans, dp[-1][k])

print(ans)