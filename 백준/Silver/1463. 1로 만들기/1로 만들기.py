# 220818 1463 1로 만들기

import sys

input = sys.stdin.readline

N =int(input())

# 1로 만들어주는 가상의 함수 f(x)
# n이 주어졌을 때 할 수 있는 동작은 3가지(3으로 나누기, 2로 나누기, 1 빼기)이므로 셋 중 최솟값을 고르면 된다.

# f(n) = min(f(n / 3), f(n / 2), f(n - 1)) + 1 (나눠떨어질 때)

# f(1) = 0
table = [0, 0]

if N == 1:
    print(table[N])
else:
    # 나눠 떨어지는지에 따라서 조건문을 설정하고 각 경우의 최소값을 구한다.
    for i in range(2, N + 1):
        if i % 3 == 0 and i % 2 == 0:
            # print(i, 1)
            table.append(min(table[i//3], table[i//2], table[i - 1]) + 1)
        elif i % 3 == 0:
            # print(i, 2)
            table.append(min(table[i//3], table[i - 1]) + 1)
        elif i % 2 == 0:
            # print(i, 3)
            table.append(min(table[i//2], table[i - 1]) + 1)
        else:
            # print(i, 4)
            table.append(table[i - 1] + 1)
        # print(table)

    # print(table)
    print(table[N])
