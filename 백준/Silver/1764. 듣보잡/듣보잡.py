# 220904 1764 듣보잡


import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())

hear = set()
see = set()

for _ in range(N):
    hear.add(input().strip())

for _ in range(M):
    see.add(input().strip())

hear_see = list(hear&see)

hear_see.sort()

print(len(hear_see))
for person in hear_see:
    print(person)