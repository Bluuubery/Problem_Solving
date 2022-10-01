from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221001 2887 행성터널

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

N = int(input())

planet = []
total_cost = 0

# 행성의 위치 정보  
for i in range(1, N + 1):
    planet.append(list(map(int, input().split())) + [i])


graph = []
for i in range(3):

    planet.sort(key=lambda x:x[i])
    
    for j in range(N - 1):
        planet_1 , planet_2 = planet[j], planet[j + 1]
        cost = abs(planet_1[i] - planet_2[i])
        graph.append((cost, planet_1[-1], planet_2[-1]))
        

graph.sort()

parent = [i for i in range(N + 1)]

total_cost = 0
for i in range(len(graph)):
    cost, node1, node2 = graph[i]
    # 부모 노드가 다르면 cylce하지 않다
    if find(node1) != find(node2):
        # mst에 포함
        merge(node1, node2)
        # 가중치 계산
        total_cost += cost
        
print(total_cost)
