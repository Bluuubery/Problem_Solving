# 220912 16234 인구이동

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    # 유니온 연합 저장, 인구수 저장
    union = []
    pop_sum = 0
    queue = deque()

    visited[r][c] = 1
    queue.append((r, c))
    union.append((r, c))
    pop_sum += arr[r][c]

    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                # 인구차이 조건
                if L <= abs(arr[nr][nc] - arr[r][c]) <= R:
                    # 방문 표시 하고 연합 추가
                    union.append((nr, nc))
                    pop_sum += arr[nr][nc]
                    
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

    return union, pop_sum


def migration(union, pop_sum):
    flag = False

    avg_pop = pop_sum // len(union)

    for r, c in union:
        if arr[r][c] != avg_pop:
            arr[r][c] = avg_pop
            flag = True

    return flag


cnt = 0
while True:
    flag = False
    for i in range(N):
        for j in range(N):
            # 방문 안햇으면 연합 찾기
            if visited[i][j] == 0:
                union, pop_sum = bfs(i, j)
                # 인구 이동
                if migration(union, pop_sum): 
                    # print(i, j, union, pop_sum)
                    # print(arr)
                    # visited 초기화
                    flag = True

    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    if flag == False:
        break
    else:
        cnt += 1
    # print(cnt)
    # print()

print(cnt)

        