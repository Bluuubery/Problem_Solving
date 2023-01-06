from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 230106 2798 블랙잭

# 정답코드

N, M = map(int, input().split())

cards = list(map(int, input().split()))

ans = 0
min_diff = 9999999

for comb in combinations(cards, 3):
    if sum(comb) == M:
        ans = M
        break

    diff = M - sum(comb)

    if diff < 0:
        continue

    if  diff < min_diff:
        min_diff = diff
        ans = sum(comb)

print(ans)