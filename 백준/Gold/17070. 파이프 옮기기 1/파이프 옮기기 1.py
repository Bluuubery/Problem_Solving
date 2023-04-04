import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230404 17070 파이프 옮기기

# 정답코드

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(1, N):

        if arr[r][c] == 1:
            # print(r, c)
            continue


        if r == 0:
            if c == 1:
                dp[r][c][0] = 1
                continue

            # 가로
            if arr[r][c - 1] == 0:
                dp[r][c][0] += dp[r][c - 1][0] + dp[r][c - 1][2]
            #대각
            if arr[r - 1][c - 1] == 0 and arr[r][c - 1] == 0 and arr[r - 1][c] == 0:
                dp[r][c][2] += dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]



        if 0 <= r - 1:
            # 가로
            if arr[r][c - 1] == 0:
                dp[r][c][0] += dp[r][c - 1][0] + dp[r][c - 1][2]
            #세로
            if arr[r - 1][c] == 0:
                dp[r][c][1] += dp[r - 1][c][1] + dp[r - 1][c][2]
            #대각
            if arr[r - 1][c - 1] == 0 and arr[r][c - 1] == 0 and arr[r - 1][c] == 0:
                dp[r][c][2] += dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]


# for row in dp:
#     print(*row)

print(sum(dp[N - 1][N - 1]))