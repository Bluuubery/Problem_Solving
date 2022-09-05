# 220905 11000 강의실 배정

# 정답코드

import heapq
import sys
input = sys.stdin.readline

N = int(input())
lecture = []
for _ in range(N):
    temp = list(map(int, input().split()))
    lecture.append(temp)

lecture.sort()

queue = []
heapq.heappush(queue, lecture[0][1])

for i in range(1, N):
    if queue[0] > lecture[i][0]:
        heapq.heappush(queue, lecture[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, lecture[i][1])

print(len(queue))