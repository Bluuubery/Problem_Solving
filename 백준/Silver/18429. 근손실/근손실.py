import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221006 18429 근손실

# 정답코드

N, K = map(int, input().split())
kit = list(map(int, input().split()))
visited = [0 for _ in range(N)]
ans = 0

def back_tracking(depth, strength):
    global ans

    if depth == N:
        ans += 1
        return
    
    for i in range(N):
        if not visited[i]:
            if strength + kit[i] - K >=0:
                visited[i] = 1
                back_tracking(depth + 1, strength + kit[i] - K)
                visited[i] = 0

    return


back_tracking(0, 0)

print(ans)