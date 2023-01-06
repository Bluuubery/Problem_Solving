# 230106 6064 카잉 달력

import math
from sys import flags


T = int(input())

for _ in range(T):

    M, N, x, y = map(int, input().split())

    ans = 1
    end_year = math.lcm(M, N)

    flag = False

    for year in range(x, end_year + 1, M):
        # print(year, year % N)
        if year % N == 0 and y == N:
            ans = year
            break

        if (year % N) == y:
            ans = year
            break
    else:
        flag = True

    if flag == True:
        print(-1)
    else:
        print(ans)      

