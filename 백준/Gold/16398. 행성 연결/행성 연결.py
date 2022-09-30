import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220927 16398 행성 연결

# 정답코드


# 최소 신장트리를 위한 유니온파인드 함수
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


N = int(input())
planets = [list(map(int, input().split())) for _ in range(N)]

parent = [i for i in range(N + 1)]

graph = []
for r in range(N - 1):
    for c in range(r + 1, N):
        graph.append((planets[r][c], r + 1, c + 1))
graph.sort()


ans = 0
for i in range(len(graph)):
    cost, node1, node2 = graph[i]
    if find(node1) != find(node2):
        merge(node1, node2)
        ans += cost

print(ans)