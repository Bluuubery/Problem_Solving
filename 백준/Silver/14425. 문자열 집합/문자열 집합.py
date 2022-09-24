N, M = map(int, input().split())

set_N = set()

for _ in range(N):
    set_N.add(input())

ans = 0
for _ in range(M):
    if input() in set_N:
        ans += 1


print(ans)

