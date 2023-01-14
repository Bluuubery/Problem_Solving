# 230114 노 땡스!

N = int(input())
cards = list(map(int, input().split()))

cards.sort()

ans = 0
score = cards[0]

for i in range(1, N):
    if cards[i] - cards[i - 1] == 1:
        continue
    else:
        ans += score
        score = cards[i]
else: 
    ans += score

print(ans)