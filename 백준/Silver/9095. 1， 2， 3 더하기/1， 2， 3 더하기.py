# 220818 9063 1, 2, 3 더하기

import sys

input = sys.stdin.readline

table = [0] * 12

table[1] = 1
table[2] = 2
table[3] = 4

for i in range(4, 12):
    table[i] = table[i - 3] + table[i - 2] + table[i - 1] 

T = int(input())

for _ in range(T):
    n = int(input())
    print(table[n])