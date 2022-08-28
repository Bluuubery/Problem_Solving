# 220828 1954 달팽이 숫자

# 정답코드

T = int(input())

for t in range(1, T + 1):
    
    # N: 달팽이 숫자 크기, arr: 달팽이 숫자를 담을 빈 배열
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    # 탐색 방향 (달팽이의 이동 방향: 우 -> 하 -> 좌 -> 상)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # r, c, d: 달팽이의 출발점 및 출발 방향
    r = 0
    c = 0
    d = 0

    # 1부터 N^2까지의 숫자를 채워 넣는다.
    for i in range(1, N**2 + 1):
        arr[r][c] = i
        
        # nr, nc: 다음 탐색 방향
        nr = r + dr[d]
        nc = c + dc[d]

        # 범위를 벗어나지 않고 0이면 다음 탐색 방향으로 이동
        if 0<= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
        # 범위를 벗어나거나 이미 다른 숫자가 있으면 방향 전환
        else:
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]         

    # 달팽이 숫자 출력
    print(f'#{t} ')
    for row in arr:
        print(*row)             