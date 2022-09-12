# 220912 16234 인구이동

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

# N: 배열의 크기, L, R: 인구이동 범위 조건
N, L, R = map(int, input().split())
# arr: 배열, visited: 방문여부 표시 배열
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

# 델타 탐색 방향 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# bfs 함수 
def bfs(r, c):
    # union: 연합 국가들의 좌표 
    # pop_sum: 연합 내 인구 수의 합
    union = []
    pop_sum = 0
    queue = deque()

    # 출발점 방문 표시 및 큐에 저장
    visited[r][c] = 1
    queue.append((r, c))

    # 출발점 연합에 포함 및 인구 수 가산
    union.append((r, c))
    pop_sum += arr[r][c]

    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위 내 포함 및 미방문
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                # 인구차이 조건 만족
                if L <= abs(arr[nr][nc] - arr[r][c]) <= R:
                    # 연합 추가 및 인구수 가산
                    union.append((nr, nc))
                    pop_sum += arr[nr][nc]
                    
                    # 방문 표시 및 큐에 좌표 저장
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

    # 연합 좌표 및 인구수 반환
    return union, pop_sum


# 인구 이동 함수
def migration(union, pop_sum):
    # flag: 인구 이동 여부
    flag = False

    # 인구 이동
    avg_pop = pop_sum // len(union)
    for r, c in union:
        if arr[r][c] != avg_pop:
            arr[r][c] = avg_pop
            # 인구 이동 표시
            flag = True

    # 인구 이동 여부 반환
    return flag


# cnt: 인구 이동 일수
cnt = 0
while True:
    # terminate: 종료 조건 변수 True로 초기화
    terminate = True

    # arr 전체 돌면서 bfs 탐색
    for i in range(N):
        for j in range(N):
            # 미방문시(연합x) bfs 탐색으로 연합 탐색
            if visited[i][j] == 0:
                union, pop_sum = bfs(i, j)
                # 연합이 없을 경우 인구 이동 x
                if len(union) > 1:
                # 인구 이동
                    if migration(union, pop_sum): 
                        # 종료 조건 변경(탐색 지속)
                        terminate = False

    # visited 배열 초기화
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    # 종료 조건 True시 탐색 종료
    if terminate == True:
        break
    # 일 수 세주기
    else:
        cnt += 1

# 정답 출력
print(cnt)

        