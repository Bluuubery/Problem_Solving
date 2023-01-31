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

# 회전 고려해서 k만큼 뒤에 추가
sushi = sushi + sushi[:k] 

ans = 0
for i in range(N):

    # 슬라이딩 윈도우
    eat = sushi[i:i + k]
    eat = set(eat)

    # 쿠폰 초밥 포함
    if c in eat:
        ans = max(ans, len(eat))
    # 미포함
    else:
        ans = max(ans, len(eat) + 1)

print(ans)