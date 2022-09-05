# 220905 13335 트럭

# 정답코드
from collections import deque
import sys
input = sys.stdin.readline

# N: 트럭의 대수, length: 다리의 길이, weight: 다리의 최대하중
N, length, weight = map(int, input().split())
# truck: 트럭의 무게
truck = list(map(int, input().split()))

# bridge: 다리 항상 length만큼의 원소를 가진다. (0으로 초기화)
bridge = deque([0] * length)

# cnt: 다리를 빠져나온 트럭의 대수, idx, 트럭의 인덱스, time: 시간(1로 초기화) 
cnt = 0
idx = 0
time = 1
while True:
    # 다리에서 0 또는 트럭이 빠져나온다.
    out = bridge.popleft()

    # 빠져나온 게 트럭이라면 cnt를 세준다.
    if out > 0:
        cnt += 1
        # 트럭에서 다리가 다 빠져나왔으면 중단
        if cnt == N:
            break
    
    # 다리에 오르지 못한 트럭이 남아있고 다음 트럭과 현재 다리의 하중의 합이 최대하중보다 낮으면 다리에 트럭이 오른다.
    if idx < N and sum(bridge) + truck[idx] <= weight:
        bridge.append(truck[idx])
        idx += 1
    # 그 외 경우에는 0을 추가해 한 칸씩 밀어준다.
    else:
        bridge.append(0)

    # 시간을 세준다.
    time += 1

# 흐른 시간 출력
print(time)