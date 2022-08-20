# 220815 2559 수열

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

temperature = list(map(int, input().split()))

max_temp = sum(temperature[0:K])
sum_temp = sum(temperature[0:K])
start = 0
end = K

while True:
    if end == N:
        break

    sum_temp = sum_temp - temperature[start] + temperature[end]

    start += 1
    end += 1
    if sum_temp > max_temp:
        max_temp = sum_temp
    # print(start + 1, sum_temp)


print(max_temp)
