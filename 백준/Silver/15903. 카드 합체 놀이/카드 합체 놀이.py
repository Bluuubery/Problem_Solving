# 220905 15903 카드 합체 놀이

# 정답코드

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))

heapq.heapify(card)

for _ in range(M):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a + b)
    heapq.heappush(card, a + b)

print(sum(card))