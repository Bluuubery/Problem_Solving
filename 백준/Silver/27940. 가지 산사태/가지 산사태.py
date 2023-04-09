import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230408 가지컵 A. 가지 산사태

# 정답코드

N, M, K = map(int, input().split())

rain_sum = 0

for i in range(M):
    t, r = map(int, input().split())

    rain_sum += r
    if rain_sum > K:
        print(i + 1, 1)
        exit()

print(-1)