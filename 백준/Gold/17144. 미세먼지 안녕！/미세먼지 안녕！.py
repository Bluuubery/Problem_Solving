# 220828 17144 미세먼지 안녕!

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]


# 공청기 위치 찾는 함수
def find_cleaner(room):
    temp = []
    for i in range(R):
        if room[i][0] == -1:
            temp.append(i)
    # top: 위쪽 공기청정기, bottom: 아래쪽 공기청정기
    top = temp[0]
    bottom = temp[1]

    return top, bottom


# 미세먼지 확산 함수
def spread_dust(room):
    # dust_room: 확산된 미세먼지를 담을 배열
    dust_room = [[0 for _ in range(C)] for _ in range(R)]
    # 탐색(확산) 방향
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(R):
        for c in range(C):
            # 미세먼지가 있는 경우
            if room[r][c] > 0:
                # cnt: 확산된 방향의 개수
                cnt = 0
                # 4방향으로 확산
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        dust_room[nr][nc] += room[r][c] // 5
                        cnt += 1
                # 남은 미세먼지의 양
                dust_room[r][c] += room[r][c] - room[r][c] // 5 * cnt
            # 공기 청정기 위치 표시
            elif room[r][c] == -1:
                dust_room[r][c] = room[r][c]
    
    return dust_room


# 공기 청정기 바람 순환 함수
def air_clean(room, top, bottom):
    
    # 위쪽 공기 순환
    def top_circuleate():
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        # 공기청정기가 먼지를 한칸씩 빨아들이는 식으로 접근
        r = top - 1
        c = 0
        d = 0

        while True:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr <= top and 0 <= nc < C:
                if room[nr][nc] == -1:
                    room[r][c] = 0
                    return 
                else:
                    room[r][c] = room[nr][nc]
                    r = nr
                    c = nc
            else:
                d += 1

    # 아래쪽 공기 순환
    def bottom_circuleate():
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        # 공기청정기 다음 칸부터 순환
        r = bottom + 1
        c = 0
        d = 0

        while True:
            nr = r + dr[d]
            nc = c + dc[d]
            if bottom <= nr < R and 0 <= nc < C:
                if room[nr][nc] == -1:
                    room[r][c] = 0
                    return 
                else:
                    room[r][c] = room[nr][nc]
                    r = nr
                    c = nc
            else:
                d += 1

    top_circuleate()
    bottom_circuleate()
    return room
    

# 공기 청정기의 위치 찾기
top, bottom = find_cleaner(room)

# 시간 T동안 미세먼지 확산 및 공기청정기 작동
for _ in range(T):   
    room = air_clean(spread_dust(room), top, bottom)

# ans: 남아있는 미세먼지의 양(공기청정기 -2 고려)
ans = 2
for r in range(R):
    for c in range(C):
        ans += room[r][c]

print(ans)

