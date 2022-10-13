from collections import deque
from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221009 17471 게리맨더링

# 정답코드


# bfs 탐색을 통해서 선거구에 포함된 구역 수랑 인구 수 계산
def bfs(group):
    # 선거구 내의 임의의 한 구역을 출발 지점으로 지정
    start = group[0]
    visited[start] = 1

    queue = deque()
    queue.append(start)

    # cnt: 선거구 내에 포함된 구역 개수
    cnt = 1
    # group_pop: 선거구의 총 인구수 합계
    group_pop = population[start]
    while queue:
        current = queue.popleft()
        # 인구 수랑 구역 개수 세주면서 인접 구역 탐색 
        for next in graph[current]:
            if next in group and not visited[next]:
                cnt += 1
                group_pop += population[next]

                visited[next] = 1
                queue.append(next)

    # 구역 개수, 인구수 반환
    return cnt, group_pop


# N: 구역의 개수, poplulation: 구역 인구 정보, numbers: 구역 번호
N = int(input())
population = [0] + list(map(int, input().split()))
numbers = [i for i in range(1, N + 1)]

# graph: 구역 연결 관계
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0] + 1):
        graph[i].append(temp[j])

# ans: 인구 차이 최솟값(충분히 큰 값으로 초기화)
ans = float('INF')
# 조합을 절반까지만 계산한다.
for i in range(1, N//2 + 1):
    for comb in combinations(numbers, i):
        # group_1, group_2: 선거구 1, 선거구 2
        group_1 = comb
        group_2 = list(set(numbers) - set(comb))

        # visited: 방문 여부 표시 배열
        visited = [0 for _ in range(N + 1)]

        # bfs 탐색을 통해서 각 선거구에 포함된 구역 수랑 인구 수 계산
        cnt_1, group_pop_1 = bfs(group_1)
        cnt_2, group_pop_2 = bfs(group_2)

        # 모든 구역이 선거구에 포함되어있을 경우
        if cnt_1 + cnt_2 == N:
            # 최솟값 갱신
            ans = min(ans, abs(group_pop_1 - group_pop_2))

# 선거구를 나눌 수 없으면 -1 출력
if ans == float('INf'):
    print(-1)
# 정답 출력
else:
    print(ans)