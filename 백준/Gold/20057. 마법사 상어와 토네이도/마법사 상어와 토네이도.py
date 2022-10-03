import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220921 20057 마법사 상어와 토네이도

# 정답코드

# directions: 모래바람 확산 좌표와 해당 좌표의 모래 비율
directions = {
    0 : [(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1), (0, -2, 5), (1, -1, 10), (1, 0, 7), (1, 1, 1), (2, 0, 2), (0, -1)],
    1 : [(-1, -1, 1), (-1, 1, 1), (0, -2, 2), (0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 10), (1, 1, 10), (2, 0, 5), (1, 0)],
    2 : [(-2, 0, 2), (-1, -1, 1), (-1, 0, 7), (-1, 1, 10), (0, 2, 5), (1, -1, 1), (1, 0, 7), (1, 1, 10), (2, 0, 2), (0, 1)],
    3 : [(-2, 0, 5), (-1, -1, 10), (-1, 1, 10), (0, -2, 2), (0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 1), (1, 1, 1), (-1, 0)]
}

# torando: 토네이도 함수
def tornado (r, c, sand, d):
    # 글로벌 변수 선언
    global lost

    # left: 남아있는 모래의 양
    left = sand
    
    # 토네이도를 시전한 칸의 모래는 0이 된다.
    arr[r][c] = 0
    
    # 모래가 비율대로 해당 좌표로 확산한다
    for direction in directions[d][:-1]:
        nr = r + direction[0]
        nc = c + direction[1]
        # 원래 모래의 양 감소
        left -= (sand * direction [2]) // 100
        
        # 범위를 벗어나지 않으면 해당 좌표에 모래를 표시해준다.
        if 0 <= nr < N and 0 <= nc < N:
            arr[nr][nc] += (sand *direction[2]) // 100
        # 범위를 벗어나는 모래는 소실된다.
        else:
            lost += (sand * direction[2]) // 100
    

    # nr, nc: 확산되고 남은 모래가 위치할 좌표 
    nr = r + directions[d][-1][0]
    nc = c + directions[d][-1][1]

    # 범위를 벗어나지 않으면 해당 좌표에 모래 표시
    if 0 <= nr < N and 0 <= nc < N:
        arr[nr][nc] += left
    # 범위 벗어나면 소실
    else:
        lost += left

    return 

# N: 배열의 크기, arr: 모래 배열
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# lost: 격자 밖으로 나가 소실된 모래의 양
lost = 0

# 델타 탐색 방향 설정
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# r, c: 시작 위치, d: 토네이도 이동 방향
r = N // 2
c = N // 2
d = 0

# change: 해당 방향으로 몇 번 이동해야 방향이 바뀌는지를 나타내는 변수
change = 1
# cnt: 해당 방향으로 이동한 횟수
cnt = 0
# flag_cnt: change 변수의 증가를 나타내는 변수
flag_cnt = 0

# 중앙에서부터 토네이도 이동
for i in range(N*N - 1):
    # 해당 방향으로 이동한 횟수를 세준다.
    cnt += 1

    # 토네이도 이동
    r += dr[d]
    c += dc[d]

    # 이동한 위치에 모래바람이 있으면 토네이도 시행
    if arr[r][c]:
        tornado(r, c, arr[r][c], d)

    # change만큼 이동 했으면 방향을 바꿔준다.
    if cnt == change:
        d = (d + 1) % 4
        # cnt: 초기화
        cnt = 0
        # flag_cnt를 세준다.
        flag_cnt += 1

        # flag_cnt가 2가 되면 change를 1 늘려주고 flag_cnt를 초기화 해준다.
        if flag_cnt == 2:
            change += 1
            flag_cnt = 0


print(lost)