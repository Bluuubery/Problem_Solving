import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220930 13418 학교 탐방하기

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

N, M = map(int, input().split())


graph = []
for _ in range(M + 1):
    node1, node2, weight = map(int, input().split())
    graph.append((weight, node2, node1))

graph.sort(reverse= True)
parent = [i for i in range(N + 1)]

cnt = 0
for i in range(len(graph)):
    distance, node1, node2 = graph[i]
    if find(node1) != find(node2):
        merge(node1, node2)
        if not distance:
            cnt += 1
    
    min_distance = cnt**2

graph.reverse()
parent = [i for i in range(N + 1)]

cnt = 0
for i in range(len(graph)):
    distance, node1, node2 = graph[i]
    if find(node1) != find(node2):
        merge(node1, node2)
        if not distance:
            cnt += 1

    max_distance = cnt**2


ans = max_distance - min_distance
print(ans)