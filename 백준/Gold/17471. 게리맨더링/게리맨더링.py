from collections import deque
from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221009 17471 게리맨더링

# 정답코드


def bfs(group):
    start = group[0]
    visited[start] = 1

    queue = deque()
    queue.append(start)

    cnt = 1
    group_pop = population[start]
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if next in group and not visited[next]:
                cnt += 1
                group_pop += population[next]

                visited[next] = 1
                queue.append(next)

    return cnt, group_pop


N = int(input())
population = [0] + list(map(int, input().split()))
numbers = [i for i in range(1, N + 1)]

graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0] + 1):
        graph[i].append(temp[j])

ans = float('INF')
for i in range(1, N//2 + 1):
    for comb in combinations(numbers, i):
        group_1 = comb
        group_2 = list(set(numbers) - set(comb))

        visited = [0 for _ in range(N + 1)]

        cnt_1, group_pop_1 = bfs(group_1)
        cnt_2, group_pop_2 = bfs(group_2)

        if cnt_1 + cnt_2 == N:
            ans = min(ans, abs(group_pop_1 - group_pop_2))

if ans == float('INf'):
    print(-1)
else:
    print(ans)