from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221225 20529 가장 가까운 세 사람의 심리적 거리

# 정답코드

T = int(input())

for _ in range(T):

    N = int(input())

    mbti = list(map(str, input().split()))

    ans = 0

    if 32 >= N:

        distance_list = []

        for comb in combinations(mbti, 3):

            mbti_1 = set(comb[0])
            mbti_2 = set(comb[1])
            mbti_3 = set(comb[2])

            distance_1 = len(mbti_1 - mbti_2)
            distance_2 = len(mbti_1 - mbti_3)
            distance_3 = len(mbti_2 - mbti_3)

            distance_list.append(distance_1 + distance_2 + distance_3)

        distance_list.sort()

        ans = distance_list[0]

    print(ans)