# 230114 N: 수 나누기 게임

import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

N = int(input())
cards = list(map(int, input().split()))

players = [-1 for _ in range(1000001)]
for i in range(N):
    players[cards[i]] = i

score = [0 for _ in range(N)]


for i in range(N):
    for j in range(2*cards[i], 1000001, cards[i]):
        if players[j] >= 0:
            score[players[j]] -= 1
            score[i] += 1 

print(*score)