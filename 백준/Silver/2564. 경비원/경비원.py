# 220820 2564 경비원

import sys

input = sys.stdin.readline

W, H = map(int, input().split())
N = int(input())

location = []
for _ in range(N + 1):
    location.append(list(map(int, input().split())))

start = location.pop()

perimeter = W * 2 + H * 2


def one_line_location(direction, loc):
    if direction == 1:
        return loc
    elif direction == 4:
        return W + loc
    elif direction == 2:
        return W + H + (W - loc)
    else:
        return W + H + W + (H - loc)


start_loc = one_line_location(start[0], start[1])

total = 0
for i in range(N):
    direction, loc = location[i][0], location[i][1]
    distance_1 = abs(start_loc - one_line_location(direction, loc))
    distance_2 = abs(perimeter - distance_1)
    # print(min(distance_1, distance_2))
    total += min(distance_1, distance_2)

print(total)







