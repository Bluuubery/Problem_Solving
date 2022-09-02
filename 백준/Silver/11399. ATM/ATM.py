# 220903 11399 ATM

# 정답코드

import sys
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))

people.sort()
for i in range(1, N):
    people[i] = people[i] + people[i - 1]

print(sum(people))