import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220927 23743 방탈출

# 정답코드


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
    return


N, M = map(int, input().split())

parent = [i for i in range(N + 2)]

graph = []
for i in range(M):
    node1, node2, time = map(int, input().split())
    graph.append((time, node1, node2))

warp = list(map(int, input().split()))
for i in range(1, N + 1):
    graph.append((warp[i - 1], i, N + 1))

graph.sort()

ans = 0
for i in range(len(graph)):
    time, node1, node2 = graph[i]
    if find(node1) != find(node2):
        merge(node1, node2)
        ans += time

print(ans)
