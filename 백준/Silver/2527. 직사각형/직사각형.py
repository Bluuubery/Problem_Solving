# 220815 2527 직사각형

import sys

input = sys.stdin.readline

for _ in range(4):
    numbers = list(map(int, input().split()))
    rectangle_1 = numbers[:4]
    rectangle_2 = numbers[4:]

    if rectangle_2[0] > rectangle_1[2] or rectangle_2[1] > rectangle_1[3] or rectangle_2[2] < rectangle_1[0] or rectangle_2[3] < rectangle_1[1]:
        print('d')
    elif rectangle_1[2] == rectangle_2[0] and rectangle_1[3] == rectangle_2[1]:
        print('c')
    elif rectangle_1[0] == rectangle_2[2] and rectangle_1[1] == rectangle_2[3]:
        print('c')
    elif rectangle_1[2] == rectangle_2[0] and rectangle_1[1] == rectangle_2[3]:
        print('c')
    elif rectangle_1[0] == rectangle_2[2] and rectangle_1[3] == rectangle_2[1]:
        print('c')
    elif rectangle_1[3] == rectangle_2[1] or rectangle_1[2] == rectangle_2[0] or rectangle_1[1] == rectangle_2[3] or rectangle_1[0] == rectangle_2[2]:
        print('b')
    else:
        print('a')


