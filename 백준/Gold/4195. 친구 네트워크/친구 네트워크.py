import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220928 4195 친구 네트워크

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
    else:
        parent[y] = x
        size[x] += size[y]



T = int(input())

for _ in range(T):
    F = int(input())
    parent =  dict()
    size = dict()

    for _ in range(F):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            size[x] = 1
        
        if y not in parent:
            parent[y] = y
            size[y] = 1

        union_parent(x, y)

        print(size[find_parent(x)])



    