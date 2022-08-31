# 220831 1931 회의실 배정

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())

time = []
for _ in range(N):
    time.append(list(map(int, input().split())))

time.sort(key= lambda x: (x[1], x[0]))

cnt = 1
use = time[0]
for i in range(1, len(time)):
    if time[i][0] >= use[1]:
        cnt += 1
        use = time[i]

print(cnt)