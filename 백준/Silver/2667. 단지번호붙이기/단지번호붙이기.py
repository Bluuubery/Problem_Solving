# 220824 2667 단지번호붙이기

# import sys

# sys.stdin.readline = input

# N: 지도의 크기, map: 지도, visited: 방문여부
N = int(input())
map = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


# 델타 탐색 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


# DFS 함수 정의
def dfs(x, y):
    # 글로벌 변수 선언
    global cnt
    
    # 방문표시
    visited[x][y] = True

    # 단지에 집이 있으면 세준다.
    if map[x][y]:
        cnt += 1

    # 델타 탐색 시행
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 탐색 가능하고, 방문하지 않았고 연결된 집이 있는 경우(같은 단지)
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and map[nx][ny] == 1:
                dfs(nx, ny)

# cnt: 단지에 포함된 집의 개수, house: 각 단지 내 집의 개수
cnt = 0
house = []

# 전체를 돌면서 집이 있고(1), 방문하지 않은 곳으로부터 탐색을 시작한다.
for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            house.append(cnt)
            cnt = 0

# print(map)
# print(visited)

# 오름차순 정렬
house.sort()
# 총 단지 수와 단지 내 집의 개수 출력
print(len(house))
for i in house:
    print(i)

