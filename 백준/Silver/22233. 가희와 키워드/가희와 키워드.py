import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 22233 가희와 키워드

M, N = map(int, input().split())

keyword = set()

for _ in range(M):
    keyword.add(input())

for _ in range(N):
    writens = input().split(',')
    
    for writen in writens:
        keyword.discard(writen)

    print(len(keyword))