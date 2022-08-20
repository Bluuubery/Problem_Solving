# 220820 2578 빙고

import sys
import pprint

input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]

call_number = [list(map(int, input().split())) for _ in range(5)]
call_number = sum(call_number, [])


def find_index(a, array):
    for i in range(5):
        for j in range(5):
            if array[i][j] == a:
                return i, j


def is_bingo(bingo):
    cnt = 0

    for row in bingo:
        if sum(row) == 0:
            cnt += 1

    for col in list(map(list, zip(*bingo[::-1]))):
        if sum(col) == 0:
            cnt += 1

    diagonal = 0
    for i in range(5):
        diagonal += bingo[i][i]
    if diagonal == 0:
        cnt += 1

    diagonal = 0
    for i in range(5):
        diagonal += bingo[i][4 - i]
    if diagonal == 0:
        cnt += 1

    # return cnt
    if cnt >= 3:
        return True
    else:
        return False


cnt = 0
while True:
    cnt += 1
    i, j = find_index(call_number[cnt - 1], bingo)
    bingo[i][j] = 0
    # print(cnt)
    # pprint.pprint(bingo)
    # print(f'is bingo: {is_bingo(bingo)}')
    # print()
    if is_bingo(bingo):
        break
    else:
        pass

print(cnt)
