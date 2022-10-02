import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221002 14950 정복자

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


N, M, T = map(int, input().split())

graph = []
for _ in range(M):
    node1, node2, weight = map(int, input().split())
    graph.append((weight, node1, node2))

graph.sort()

parent = [i for i in range(N + 1)]

cnt = 0
total_cost = 0
for i in range(M):
    cost, node1, node2 = graph[i]
    if find(node1) != find(node2):
        merge(node1, node2)
        total_cost += cost + (cnt * T)
        cnt += 1

print(total_cost)