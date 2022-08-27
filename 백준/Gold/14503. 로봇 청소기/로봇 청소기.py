# 220827 14503 로봇 청소기

# 정답코드

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


room[r][c] = -1
# print(room)
cnt = 1
while True:
    nr = r + dr[d]
    nc = c + dc[d]

    if room[nr][nc] == 0:
        r = nr
        c = nc
        room[r][c] = -1
        if d == 0:
            d = 3
        else:
            d -= 1
        cnt += 1
    
    else:
        for i in range(1, 4):
            if d - i < 0:
                nd = d - i + 4
            else:
                nd = d - i

            nr = r + dr[nd]
            nc = c + dc[nd]
            if room[nr][nc] == 0:
                d = nd                
                break
        else:
            if d == 0:
                if room[r + 1][c] == 1:
                    break
                else:
                    r = r + 1
                    c = c
            elif d == 1:
                if room[r][c - 1] == 1:
                    break
                else:
                    r = r
                    c = c - 1
            elif d == 2:
                if room[r - 1][c] == 1:
                    break
                else:
                    r = r - 1
                    c = c
            elif d == 3:
                if room[r][c + 1] == 1:
                    break
                else:
                    r = r
                    c = c + 1

# for row in room:
#     print(row)
# print(room)
print(cnt)