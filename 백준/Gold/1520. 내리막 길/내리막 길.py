import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

sys.setrecursionlimit(10**5)
# 220925 1520 내리막길

# 정답코드

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dp = [[-1 for _ in range(C)] for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def dfs(r, c):

    if r == R - 1 and c == C - 1:
        return 1
    
    if dp[r][c] != -1:
        return dp[r][c]

    
    dp[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < R and 0 <= nc < C:
            if arr[nr][nc] < arr[r][c]:
                dp[r][c] += dfs(nr, nc)

    return dp[r][c]


print(dfs(0, 0))