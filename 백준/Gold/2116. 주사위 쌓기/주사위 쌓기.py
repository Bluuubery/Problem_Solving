# 220815 2116 주사위 쌓기

import sys

input = sys.stdin.readline


def up_and_max_side(bottom: int, dice:list):
    # idx = dice.index(bottom)
    for i in range(6):
        # 윗면과 아랫면 맞추기
        if dice[i] == bottom:
            idx = i
            break
      # print(idx)
    if idx == 0:
        return dice[5], max(dice[1], dice[2], dice[3], dice[4])
    elif idx == 1:
        return dice[3], max(dice[0], dice[2], dice[4], dice[5])
    elif idx == 2:
        return dice[4], max(dice[0], dice[1], dice[3], dice[5])
    elif idx == 3:
        return dice[1], max(dice[0], dice[2], dice[4], dice[5])
    elif idx == 4:
        return dice[2], max(dice[0], dice[1], dice[3], dice[5])
    elif idx ==5:
        return dice[0], max(dice[1], dice[2], dice[3], dice[4])

N = int(input())

# 0-5 1-3 2-4
dices = []
for _ in range(N):
    dice = list(map(int, input().split()))
    dices.append(dice)

max_sum = 0
for i in range(1, 7):
    # print(f'start:{i}')
    start = i
    side_sum = 0
    for j in range(0, N):
        start, side = up_and_max_side(start, dices[j])
        side_sum += side
    if max_sum < side_sum:
        max_sum = side_sum

print(max_sum)
