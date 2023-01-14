# 230114 B: 할리갈리

from collections import defaultdict

ans = 'NO'

N = int(input())
fruit_dict = defaultdict(int)

for _ in range(N):
    fruit, num = input().split()
    fruit_dict[fruit] += int(num)

for cnt in fruit_dict.values():
    if cnt == 5:
        ans = 'YES'
        break

print(ans)