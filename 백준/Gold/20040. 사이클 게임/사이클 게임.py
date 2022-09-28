import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220928 20040 사이클 게임

# 정답코드


def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return x


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x == y:
        return True

    if x < y:
        parent[y] = x
        
    else:
        parent[x] = y
    return False


def solve():
    for i in range(1, M + 1):
        a, b = map(int, input().split())
        if union_parent(a, b):
            print(i)
            return
    
    print(0)
    return

N, M = map(int, input().split())
parent = [i for i in range(N)]

solve()
