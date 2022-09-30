from collections import defaultdict
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220927 8980 택배

# 정답코드

N, C = map(int, input().split())
M = int(input())

freight = [tuple(map(int, input().split())) for _ in range(M)]

freight.sort(key=lambda x :(x[1], x[0]))

capcity = [C for _ in range(N + 1)]

ans = 0

for i in range(M):
    start, end, box = freight[i]

    load = min(C, min(capcity[start:end]))
    load = min(load, box)

    for j in range(start, end):
        capcity[j] -= load

    ans += load
    

print(ans)    
