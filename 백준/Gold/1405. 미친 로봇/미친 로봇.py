import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220923 1405 미친 로봇

# 정답코드

probability = list(map(int, input().split()))
N = probability.pop(0)

arr = [[0 for _ in range(29)] for _ in range(29)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def back_tracking(r, c, depth, p):
    global ans 

    if depth == N:
        ans += p / (100**N)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not arr[nr][nc]:
            arr[nr][nc] = 1

            back_tracking(nr, nc, depth + 1, p * probability[i])

            arr[nr][nc] = 0

    else:
        return


ans = 0
arr[14][14] = 1
back_tracking(14, 14, 0, 1)

print(ans)