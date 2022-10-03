import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221003 1185 유럽여행

# 정답코드

# find 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# union 함수
def merge(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
        
    else:
        parent[x] = y

    return

N, P = map(int, input().split())

cost = [0]
for _ in range(N):
    cost.append(int(input()))

graph = []
for _ in range(P):
    node1, node2, weight = map(int, input().split())
    graph.append((weight * 2 + cost[node1] + cost[node2], node1, node2))
graph.sort()

parent = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]

total_cost = 0
for i in range(P):
    weight, node1, node2 = graph[i]

    if find(node1) != find(node2):
        merge(node1, node2)
        total_cost += weight

print(total_cost + min(cost[1:]))