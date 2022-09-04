# 220904 11501 주식

# 정답코드
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    stock_price = list(map(int, input().split()))
    stock_price = stock_price[::-1]

    ans = 0
    max_price = stock_price[0]
    for i in range(1, N):
        if stock_price[i] > max_price:
            max_price = stock_price[i]
        else:
            ans += max_price - stock_price[i]

    
    print(ans)