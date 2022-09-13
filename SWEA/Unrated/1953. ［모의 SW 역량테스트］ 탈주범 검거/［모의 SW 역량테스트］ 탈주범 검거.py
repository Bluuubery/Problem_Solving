# 220913
# 1953 탈주범 검거

# 정답코드

from collections import deque


# 파이프별 방향 정보
dir_dict = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0), (0, 0), (0, 0)],
    3: [(0, 0), (0, 0), (0, -1), (0, 1)],
    4: [(-1, 0), (0, 0), (0, 0), (0, 1)],
    5: [(0, 0), (1, 0), (0, 0), (0, 1)],
    6: [(0, 0), (1, 0), (0, -1), (0, 0)],
    7: [(-1, 0), (0, 0), (0, -1), (0, 0)],
}


# bfs 함수 선언
# cnt: 현재까지 이동 시간
def bfs(r, c, L, cnt):

    # 방문 표시
    visited[r][c] = 1
    # move: 탈주범 이동 위치(위치할 수 있는 장소의 개수)
    move = 1
    
    queue = deque()
    queue.append((r, c, cnt))

    while queue:
        r, c, cnt = queue.popleft()

        # 시간이 다 됐으면 정답 출력
        if cnt == L:
            print('#{} {}'.format(t, move))
            return

        # 파이프에 따른 방향 설정
        dr = dir_dict[arr[r][c]]
        
        for i in range(4):
            nr = r + dr[i][0]
            nc = c + dr[i][1]

            if 0 <= nr < N and 0 <= nc < M:
                # 아직 미방문 구역일 경우
                if visited[nr][nc] == 0:
                    # 파이프가 존재할 경우
                    if arr[nr][nc] > 0:
                        # 파이프가 다음 파이프와 이어질 경우 (방향의 부호를 바꿔주면 된다)
                        if (-dr[i][0], -dr[i][1]) in dir_dict[arr[nr][nc]]:

                            # 방문 표시 및 탈주범 이동
                            visited[nr][nc] = 1
                            move += 1

                            queue.append((nr, nc, cnt + 1))
    
    # 다 이동했을 경우에도 정답 출력
    print('#{} {}'.format(t, move))
    return


# T: 테스트 케이스 개수
T = int(input())
for t in range(1, T + 1):

    # N, M: 배열 크기
    # R, C: 맨홀 위치(시작 위치)
    # L: 소요 시간
    N, M, R, C, L = map(int, input().split())

    # arr: 배열, visited: 방문 여부 표시 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    # bfs 탐색 실시
    bfs(R, C, L, 1)
