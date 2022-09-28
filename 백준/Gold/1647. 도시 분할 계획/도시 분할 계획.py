import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220928 1647 도시 분할 계획

# 정답코드

# V: 정점 개수, E: 간선 개수
V, E = map(int, input().split())

# parent: 부모 테이블 (자기 자신으로 초기화)
parent = [i for i in range(V + 1)]


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

# edges: 간선 정보를 담을 리스트, total_cost: 최소 신장 트리의 가중치 합계
edges = []
total_cost = 0

# 간선 정보 입력 
for _ in range(E):
    node1, node2, cost = map(int, input().split())
    edges.append((cost, node1, node2))

# 가중치 기준으로 정렬
edges.sort()


# 각 간선에 대해 유니온-파인드로 cylce 여부 판단하여 크루스칼 알고리즘 수행
for i in range(E):
    cost, node1, node2 = edges[i]
    # 부모 노드가 다르면 cylce하지 않다
    if find(node1) != find(node2):
        # mst에 포함
        merge(node1, node2)
        # 가중치 계산
        total_cost += cost

        # 연결을 끊을 간선
        disconnect = cost

# 도시를 분리한다.
total_cost -= disconnect

# 가중치 합계 출력
print(total_cost)