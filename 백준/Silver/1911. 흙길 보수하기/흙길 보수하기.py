import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221012 1911 흙길 보수하기

# 정답코드

N, L = map(int, input().split())
puddle = [tuple(map(int, input().split())) for _ in range(N)]
puddle.sort()

current = puddle[0][0]
ans = 0
for start, end in puddle:
    if current >= end:
        continue

    if start > current:
        current = start
    
    
    
    if (end - current) % L == 0:
        ans += (end - current)// L
        current += end - current
    else:
        ans += (end - current) // L + 1
        current += ((end - current) // L + 1) * L

print(ans)