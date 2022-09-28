import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
sys.setrecursionlimit(10**5)


# 220928 1717 집합의 표현

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


N, M = map(int, input().split())

parent = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    flag, a, b = map(int, input().split())

    if flag == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('yes')
        else:
            print('no')


