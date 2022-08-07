# 220807 swea 1859 백만장자프로젝트
t = int(input())

for i in range(t):
    n = int(input())
    price = list(map(int, input().split()))[::-1]

    profit = 0
    max_price = price[0]

    for j in range(1, n):
        if max_price > price[j]:
            profit += max_price - price[j]
        else:
            max_price = price[j]

    print(f'#{i + 1} {profit}')