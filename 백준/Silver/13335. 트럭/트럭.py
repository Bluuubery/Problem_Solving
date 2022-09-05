# 220905 13335 트럭

# 정답코드
from collections import deque
import sys
input = sys.stdin.readline

N, length, weight = map(int, input().split())
truck = list(map(int, input().split()))

bridge = deque([0] * length)

cnt = 0
idx = 0
time = 1
while True:
    out = bridge.popleft()
    if out > 0:
        cnt += 1

    if idx < N and sum(bridge) + truck[idx] <= weight:
        bridge.append(truck[idx])
        idx += 1
    else:
        bridge.append(0)

    if cnt == N:
        break
    
    time += 1

print(time)