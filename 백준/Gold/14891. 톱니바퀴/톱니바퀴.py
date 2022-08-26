# 220826 14891 톱니바퀴

from collections import deque
import sys

# input = sys.stdin.readline




def rotate(gear: list, gear_num: int, direction: int):
    if gear_num == 1:
        if (gear[0][2] != gear[1][6]) and (gear[1][2] != gear[2][6]) and (gear[2][2] != gear[3][6]):
            # print(1, 1)
            gear[0].rotate(direction)
            gear[1].rotate(-direction)
            gear[2].rotate(direction)
            gear[3].rotate(-direction)
        elif (gear[0][2] != gear[1][6]) and (gear[1][2] != gear[2][6]):
            # print(1, 2)
            gear[0].rotate(direction)
            gear[1].rotate(-direction)
            gear[2].rotate(direction)
        elif gear[0][2] != gear[1][6]:
            # print(1, 3)
            gear[0].rotate(direction)
            gear[1].rotate(-direction)
        else:
            # print(1, 4)
            gear[0].rotate(direction)
            
    elif gear_num == 2:
        if (gear[0][2] != gear[1][6]) and (gear[1][2] != gear[2][6]) and (gear[2][2] != gear[3][6]):
            # print(2, 1)
            gear[0].rotate(-direction)
            gear[1].rotate(direction)
            gear[2].rotate(-direction)
            gear[3].rotate(direction)
        elif (gear[1][2] != gear[2][6]) and (gear[2][2] != gear[3][6]):
            # print(2, 2)
            gear[1].rotate(direction)
            gear[2].rotate(-direction)
            gear[3].rotate(direction)
        elif (gear[0][2] != gear[1][6]) and (gear[1][2] != gear[2][6]):
            # print(2, 4)
            gear[0].rotate(-direction)
            gear[1].rotate(direction)
            gear[2].rotate(-direction)
        elif gear[1][2] != gear[2][6]:
            # print(2, 3)
            gear[1].rotate(direction)
            gear[2].rotate(-direction)
        elif gear[0][2] != gear[1][6]:
            # print(2, 5)
            gear[0].rotate(-direction)
            gear[1].rotate(direction)
        else:
            # print(2, 6)
            gear[1].rotate(direction)
    
    elif gear_num == 3:
        if (gear[0][2] != gear[1][6]) and (gear[1][2] != gear[2][6]) and (gear[2][2] != gear[3][6]):
            # print(3, 1)
            gear[0].rotate(direction)
            gear[1].rotate(-direction)
            gear[2].rotate(direction)
            gear[3].rotate(-direction)
        elif (gear[1][2] != gear[2][6]) and (gear[2][2] != gear[3][6]):
            # print(3, 2)
            gear[1].rotate(-direction)
            gear[2].rotate(direction)
            gear[3].rotate(-direction)
        elif (gear[0][2] != gear[1][6]) and (gear[1][2] != gear[2][6]):
            # print(3, 4)
            gear[0].rotate(direction)
            gear[1].rotate(-direction)
            gear[2].rotate(direction)
        elif gear[2][2] != gear[3][6]:
            # print(3, 3)
            gear[2].rotate(direction)
            gear[3].rotate(-direction)
        elif gear[1][2] != gear[2][6]:
            # print(3, 5)
            gear[1].rotate(-direction)
            gear[2].rotate(direction)
        else:
            # print(3, 6)
            gear[2].rotate(direction)

    else: 
        if (gear[0][2] != gear[1][6]) and (gear[1][2] != gear[2][6]) and (gear[2][2] != gear[3][6]):
            # print(4, 1)
            gear[0].rotate(-direction)
            gear[1].rotate(direction)
            gear[2].rotate(-direction)
            gear[3].rotate(direction)
        elif (gear[1][2] != gear[2][6]) and (gear[2][2] != gear[3][6]):
            # print(4, 2)
            gear[1].rotate(direction)
            gear[2].rotate(-direction)
            gear[3].rotate(direction)
        elif gear[2][2] != gear[3][6]:
            # print(4, 3)
            gear[2].rotate(-direction)
            gear[3].rotate(direction)
        else:
            # print(4, 4)
            gear[3].rotate(direction)


# gear: 톱니바퀴
gear = []
for _ in range(4):
    gear.append(deque(map(int, input())))



# K: 회전 수
K = int(input())
# rotate_info[0]: 회전시킬 톱니바퀴 번호, rotate_info[1]: 회전 방향
rotate_info = []
for _ in range(K):
    rotate_info.append(list(map(int, input().split())))

for i in range(K):
    rotate(gear, rotate_info[i][0], rotate_info[i][1])
    # print(gear)


ans = 0
if gear[0][0] == 1:
    ans += 1
if gear[1][0] == 1:
    ans += 2
if gear[2][0] == 1:
    ans += 4
if gear[3][0] == 1:
    ans += 8

print(ans)