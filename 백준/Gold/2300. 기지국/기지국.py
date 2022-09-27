import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220927 2300 기지국

# 정답코드

N = int(input())

station = []
for _ in range(N):
    temp = list(map(int, input().split()))
    temp[1] = abs(temp[1])
    station.append(temp)

station.sort()

dp = [sys.maxsize for _ in range(10001)]

dp[0] = 0
dp[1] = station[0][1] * 2


for i in range(2, N + 1):
    height = station[i - 1][1]
    for j in range(i - 1, -1, -1):
        height = max(height, station[j][1])
        dp[i] = min(dp[i], dp[j] + max(height * 2, station[i - 1][0] - station[j][0]))

print(dp[N])