# 220904 13305 주유소

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
city = list(map(int, input().split()))

oil_price = city[0]

ans = 0
for i in range(N - 1):
    if city[i] < oil_price:
        oil_price = city[i]
    ans += oil_price * distance[i]

print(ans)
