import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220930 10423 전기가 부족해

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

    if x in station:
        parent[y] = x
    
    elif y in station:
        parent[x] = y
    
    elif x < y:
        parent[y] = x
        
    else:
        parent[x] = y

    return


N, M, K = map(int, input().split())
station = list(map(int, input().split()))

parent = [i for i in range(N + 1)]

graph = []
for i in range(M):
    node1, node2, cost = map(int, input().split())
    graph.append((cost, node1, node2))

graph.sort()

total_cost = 0
for cost, node1, node2 in graph:
    if find(node1) in station and find(node2) in station:
        continue

    if find(node1) != find(node2):
        merge(node1, node2)
        total_cost += cost

print(total_cost)
