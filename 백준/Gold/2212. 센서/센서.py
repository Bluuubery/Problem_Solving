# 220903 2212 센서

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))

sensor = list(set(sensor))
sensor.sort()

if K >= len(sensor):
    print(0)
    exit(0)

distance = [0]
for i in range(1, len(sensor)):
    distance.append(sensor[i] - sensor[i-1])

distance.sort(reverse=True)
total_distance = sum(distance)

# distance = list(enumerate(distance))
# distance.sort(key= lambda x: x[1], reverse=True)

for i in range(K - 1):
    total_distance -= distance[i]

print(total_distance)
