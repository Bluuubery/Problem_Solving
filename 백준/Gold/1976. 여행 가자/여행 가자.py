import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220928 1976 여행가자

# 정답코드

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return 
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return



N = int(input())
M = int(input())

graph = [(list(map(int, input().split()))) for _ in range(N)]
plan = list(map(int, input().split()))

parent = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    parent[i] = i

for r in range(N):
    for c in range(N):
        if graph[r][c]:
            union_parent(r + 1, c + 1)

ans = 'YES'
for i in range(M - 1):
    if find_parent(plan[i]) != find_parent(plan[i + 1]):
        ans = 'NO'

print(ans)


