from collections import defaultdict, deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221003 2637 장난감 조립

# 정답코드

N = int(input())
M = int(input())

indegree = [0 for _ in range(N + 1)]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    part1, part2, cnt = map(int, input().split())
    graph[part2].append([part1, cnt])
    indegree[part1] += 1

queue = deque()
basic = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        basic.append(i)

arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

while queue:
    current = queue.popleft()

    for next in graph[current]:
        if current in basic:
            arr[next[0]][current] += next[1]
        else:
            for i in range(1, N + 1):
                arr[next[0]][i] += arr[current][i] * next[1]

        indegree[next[0]] -= 1

        if indegree[next[0]] == 0:
            queue.append(next[0])


for idx, parts in enumerate(arr[N]):
    if parts:
        print(idx, parts)
