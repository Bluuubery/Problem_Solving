# 220821 10157 자리배정

import sys

input = sys.stdin.readline

# C: 가로, R: 세로, K: 관객 번호
C, R = map(int, input().split())
K = int(input())

# 인덱스 출력 형태가 배열을 시계 방향으로 90도 돌려서 계산하는 게 더 편리하다

# 애초에 번호가 넘어간 경우엔 바로 0 출력
if K > C * R:
    print(0)
else:
    # 탐색 방향 (우 -> 하 -> 좌 -> 상)
    direction_x = [0, 1, 0, -1]
    direction_y = [1, 0, -1, 0]
    
    # 90도 돌린 배열 0으로 초기화
    seat = [[0 for _ in range(R)] for _ in range(C)]
    
    # 출발 위치, 처음 탐색 방향 설정
    x = 0
    y = 0
    d = 0
    
    # 목표로 하는 좌석 번호 직전 번호까지만 채운다(좌석번호까지 채우면 마지막에 좌표가 한번 더 이동한다)
    for k in range(1, K):
        seat[x][y] = k

        x += direction_x[d]
        y += direction_y[d]
        
        # 범위를 벗어나거나 이미 좌석이 배정된 경우에 탐색 방향 변경
        if not(0 <= x < C and 0 <= y < R and seat[x][y] == 0):
            x -= direction_x[d]
            y -= direction_y[d]

            d = (d + 1) % 4
            x += direction_x[d]
            y += direction_y[d]
    
    # 좌석 번호(인덱스) 출력
    print(x + 1, y + 1)
