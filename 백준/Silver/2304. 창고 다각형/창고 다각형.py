# 220815 2304 창고 다각형

import sys

input = sys.stdin.readline

N = int(input())

pillar = [list(map(int, input().split())) for _ in range(N)]

# pillar.sort(key=lambda x: x[0])

store = [0] * 1001

for i in range(len(pillar)):
    store[pillar[i][0]] = pillar[i][1]

# print(store)

highest = max(pillar, key=lambda x: x[1])

for i in range(highest[0] - 1):
    if store[i] > store[i + 1]:
        store[i + 1] = store[i]
# print(store)


for i in range(1000, highest[0], -1):
    if store[i] > store[i - 1]:
        store[i - 1] = store[i]
# print(store)

print(sum(store))