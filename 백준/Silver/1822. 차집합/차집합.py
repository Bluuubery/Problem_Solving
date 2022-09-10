# 220910 1822 차집합

# 정답코드

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

diff_set = set_A - set_B

if diff_set:
    print(len(diff_set))
    diff_list = sorted(list(diff_set))
    print(*diff_list)
else:
    print(0)