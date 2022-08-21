# 220821 2635 수 이어가기

import sys

input = sys.stdin.readline

N = int(input())

max_seq = []
for i in range(1, N + 1):
    sequence = [N, i]
    while True:
        if sequence[-2] - sequence[-1] < 0:
            break
        else:
            sequence.append(sequence[-2] - sequence[-1])

    if len(sequence) > len(max_seq):
        max_seq = sequence

print(len(max_seq))
print(*max_seq)


