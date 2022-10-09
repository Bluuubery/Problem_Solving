import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221008 12100 2048(Easy)

# 정답코드

# rotate: 배열 회전 시키는 함수 
def rotate(d):
    global arr
    # 시계방향 0도
    if d == 0:
        return

    # 시계방향 90도
    elif d == 1:
        arr = list(map(list, zip(*arr[::-1])))
        return

    # 시계방향 180도
    elif d == 2:
        arr = [[arr[N - r - 1][N - c - 1] for c in range(N)] for r in range(N)]
        return

    # 시계방향 270도    
    else:
        arr = list(map(list, zip(*arr)))[::-1]
        return


# merge: 블럭들을 합치는 함수 (행 단위)
def merge():
    
    for row in arr:
        for i in range(N - 1, 0, -1):
            # 직전 블럭과 같은 숫자일 경우
            if row[i] == row[i - 1]:
                # 해당 블럭 *2, 직전 블럭 0
                row[i] *= 2
                row[i - 1] = 0


# move: 블럭들을 한 방향으로 밀어주는 함수 (행 단위)
def move():

    for i in range(N):
        # new_row: 한 방향으로 밀린 새로운 행
        new_row = []
        # 0이 아니면 new_row에 담아준다.
        for j in range(N):
            if arr[i][j]:
                new_row.append(arr[i][j])

        # new_row앞에 0을 붙이고 원래 행이랑 바꿔준다. 
        arr[i] = [0] * (N - len(new_row)) + new_row


# 백트래킹 함수 
def back_tracking(depth):
    global ans, arr

    # 5번 다 이동했을 때 최댓값 갱신 후 반환
    if depth == 5:
        ans = max(ans, max(map(max, arr)))
        return
    
    # 상하좌우 4방향으로 블럭 이동
    for d in range(4):
        # arr_copy: 백트래킹 시 원상태 복원을 위한 복사본
        arr_copy = [arr[i][:] for i in range(N)]

        # 주어진 방향으로 배열 회전
        rotate(d)

        # 이동(합치기 위한 전처리) - 합치기 - 이동
        move()
        merge()
        move()

        # 다음 시행으로 넘어간다.
        back_tracking(depth + 1)

        # 배열 상태 복원
        arr = arr_copy


# N: 배열의 크기, arr: 배열 초기 상태
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# ans: 블럭의 최댓값
ans = 0

# 백트래킹 시행
back_tracking(0)

# 정답 출력
print(ans)

