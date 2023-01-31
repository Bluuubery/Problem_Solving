import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 2531 회전초밥

N, d, k, c = map(int, input().split())

sushi = list()

for _ in range(N):
    sushi.append(int(input()))

sushi = sushi + sushi[:k] 

ans = 0
for i in range(N):

    eat = sushi[i:i + k]
    # print(eat)
    eat = set(eat)

    if c in eat:
        ans = max(ans, len(eat))
    else:
        ans = max(ans, len(eat) + 1)

# print(sushi)
print(ans)