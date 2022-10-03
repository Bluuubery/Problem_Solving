from bisect import bisect_left
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221003 2352 반도체 설계

# 정답코드

N = int(input())
port = list(map(int, input().split()))

lis = []

for i in range(N):

    idx = bisect_left(lis, port[i])

    if len(lis) <= idx:
        lis.append(port[i])

    else:
        lis[idx] = port[i]

print(len(lis))
