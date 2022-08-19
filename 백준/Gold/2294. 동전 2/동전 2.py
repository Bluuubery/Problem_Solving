# 220819 2294 동전 2

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))

# 동전 사용 갯수를 담을 리스트(최솟값으로 비교할 것이므로 10001로 초기화 해준다.)
coin_sum = [10001 for _ in range(100001)]

# 각 동전에 대해서 사용 갯수를 세면서 최솟값을 갱신해 갯수 리스트에 넣어준다..
for i in range(N):
    # 초기값: 각 동전에 대해서 해당 동전의 액면가를 나타내기 위해 필요한 동전의 갯수는 1개이다
    coin_sum[coin[i]] = 1
    for j in range(coin[i], K + 1):
        # j: 만들고자 하는 금액, coin[i]: 사용할 동전
        # coin_sum[j]: 다른 동전들(!= coin[i])로 금액 j를 만들기 위한 갯수 or 기본값(10001)
        # coin_sum[j - coin[i]] + 1: 금액(j - coin[i])을 만들기 위해 필요한 동전의 갯수 + 1(coin[i] 동전 한 개 더 사용)
        coin_sum[j] = min(coin_sum[j], coin_sum[j - coin[i]] + 1)


if coin_sum[K] < 10001:
    print(coin_sum[K])
else:
    print(-1)
