import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220927 1368 물대기

# 정답코드


# find 함수 (경로 압축)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# 유니온 함수
def merge(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
    return

# N: 논의 수
N = int(input())
# parent: 부모 노드 (N + 1까지)
parent = [i for i in range(N + 2)]

# graph: 인접행렬ㄹ 나타낸 그래프
graph = []
# 우물을 나타내는 가상의 노드(N + 1)을 만들어서 우물 비용을 간선 비용으로 해서 그래프에 넣어준다.
for i in range(1, N + 1):
    graph.append((int(input()), N + 1, i))

# arr: 간선 간 연결 정보
arr = [list(map(int, input().split())) for _ in range(N)]
for r in range(N - 1):
    for c in range(r + 1, N):
        graph.append((arr[r][c], r + 1, c + 1))

# 간선 비용 정렬
graph.sort()

# ans: 물을 대는데 필요한 최소비용
ans = 0

# 최소 신장 트리로 비용 구하기
for i in range(len(graph)):
    cost, node1, node2 = graph[i]
    if find(node1) != find(node2):
        merge(node1, node2)
        ans += cost

# 정답 출력
print(ans)
