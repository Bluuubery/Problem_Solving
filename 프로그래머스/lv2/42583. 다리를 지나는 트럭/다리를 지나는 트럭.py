from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    truck_cnt = len(truck_weights)
    cnt = 0
    current_weight = 0

    while True:
        
        out = bridge.popleft()

        if out > 0:
            cnt += 1
            current_weight -= out
            if cnt == truck_cnt:
                break

        if truck_weights and weight >= current_weight + truck_weights[0]:
            in_truck = truck_weights.popleft()
            bridge.append(in_truck)
            current_weight += in_truck
        else:
            bridge.append(0)

        answer += 1    

    return answer
