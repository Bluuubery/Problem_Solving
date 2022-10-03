import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220921 20057 마법사 상어와 토네이도

# 정답코드



def tornado (r, c, sand, d):
    global lost

    left = sand
    arr[r][c] = 0

    if d == 0:
        directions = [(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1), (0, -2, 5), (1, -1, 10), (1, 0, 7), (1, 1, 1), (2, 0, 2)]
        for direction in directions:
            nr = r + direction[0]
            nc = c + direction[1]
            left -= (sand * direction [2]) // 100
            
            if 0 <= nr < N and 0 <= nc < N:
                arr[nr][nc] += (sand *direction[2]) // 100
            else:
                lost += (sand * direction[2]) // 100
        
        nr = r
        nc = c - 1
        if 0 <= nr < N and 0 <= nc < N:
            arr[nr][nc] += left
        else:
            lost += left

    elif d == 1:
        directions = [(-1, -1, 1), (-1, 1, 1), (0, -2, 2), (0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 10), (1, 1, 10), (2, 0, 5)]

        for direction in directions:
            nr = r + direction[0]
            nc = c + direction[1]
            left -= (sand * direction [2]) // 100
            
            if 0 <= nr < N and 0 <= nc < N:
                arr[nr][nc] += (sand *direction[2]) // 100
            else:
                lost += (sand * direction[2]) // 100

        nr = r + 1
        nc = c
        if 0 <= nr < N and 0 <= nc < N:
            arr[nr][nc] += left
        else:
            lost += left

    elif d == 2:
        directions = [(-2, 0, 2), (-1, -1, 1), (-1, 0, 7), (-1, 1, 10), (0, 2, 5), (1, -1, 1), (1, 0, 7), (1, 1, 10), (2, 0, 2)]

        for direction in directions:
            nr = r + direction[0]
            nc = c + direction[1]
            left -= (sand * direction [2]) // 100
            
            if 0 <= nr < N and 0 <= nc < N:
                arr[nr][nc] += (sand *direction[2]) // 100
            else:
                lost += (sand * direction[2]) // 100

        nr = r
        nc = c + 1
        if 0 <= nr < N and 0 <= nc < N:
            arr[nr][nc] += left
        else:
            lost += left

    else:
        directions = [(-2, 0, 5), (-1, -1, 10), (-1, 1, 10), (0, -2, 2), (0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 1), (1, 1, 1)]

        for direction in directions:
            nr = r + direction[0]
            nc = c + direction[1]
            left -= (sand * direction [2]) // 100
            
            if 0 <= nr < N and 0 <= nc < N:
                arr[nr][nc] += (sand *direction[2]) // 100
            else:
                lost += (sand * direction[2]) // 100

        nr = r - 1
        nc = c
        if 0 <= nr < N and 0 <= nc < N:
            arr[nr][nc] += left
        else:
            lost += left
    
    return 

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
lost = 0

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

r = N // 2
c = N // 2
d = 0
# tornado(N//2, N//2 - 1, arr[N//2][N//2 - 1], 0)
# for i in arr:
#     print(i)
# print(lost)
change = 1
change_cnt = 0

flag_cnt = 0


for i in range(N*N - 1):
    change_cnt += 1

    nr = r + dr[d]
    nc = c + dc[d]

    if arr[nr][nc]:
        tornado(nr, nc, arr[nr][nc], d)

    # print(i, d)
    # print(nr, nc)
    # for j in arr:
    #     print(j)


    r = nr
    c = nc

    if change_cnt == change:
        d = (d + 1) % 4
        change_cnt = 0
        flag_cnt += 1

        if flag_cnt == 2:
            change += 1
            flag_cnt = 0



print(lost)