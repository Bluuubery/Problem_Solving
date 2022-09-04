# 220904 13305 주유소

# 정답코드

import sys
input = sys.stdin.readline

# N: 도시 개수, distance: 도시 간 거리, station: 주유소 기름 가격
N = int(input())
distance = list(map(int, input().split()))
station = list(map(int, input().split()))

# oil_pirce: 기름 가격(첫 주유소의 가격으로 초기화)
oil_price = station[0]

# ans: 정답을 담을 변수
ans = 0
# 기름 가격을 저장해뒀다가 도시마다 비교해가면서 가격 갱신 후 주유
for i in range(N - 1):
    if station[i] < oil_price:
        oil_price = station[i]
    ans += oil_price * distance[i]

print(ans)
