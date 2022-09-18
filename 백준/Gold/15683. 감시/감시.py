from copy import deepcopy
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220918 15683 감시

# 정답코드

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


direction_dict = {
    1: [(0,), (1,), (2,), (3,)],
    2: [(0, 1), (2, 3)],
    3: [(0, 3), (3, 1), (1, 2), (2, 0)],
    4: [(2, 0, 3), (0, 3, 1), (3, 1, 2), (1, 2, 0)],
    5: [(0, 1, 2, 3)],
}



K = 0
cctv = []
cctv_dict = dict()
for r in range(N):
    for c in range(M):
        if arr[r][c] != 0 and arr[r][c] != 6:
            cctv.append((r, c))
            cctv_dict[(r, c)] = arr[r][c]
            K += 1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


ans = sys.maxsize



def check(r, c, direction, arr_copy):

    for i in direction:
        nr, nc = r, c
        while True:
            nr += dr[i]
            nc += dc[i]

            if not(0 <= nr < N and 0 <= nc < M) or arr[nr][nc] == 6:
                break
            elif arr[nr][nc] ==0:
                arr_copy[nr][nc] = 7

    return 
    


def count_blind(arr):
    cnt = 0
    for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
    return cnt


def back_tracking(cctv_list, depth, current_arr):
    global ans

    if depth == K:
        ans = min(ans, count_blind(current_arr))

        return

    r, c = cctv_list[depth]
    cctv_type = cctv_dict[(r, c)]

    arr_copy = deepcopy(current_arr)

    for direction in direction_dict[cctv_type]:
        check(r, c, direction, arr_copy)

        back_tracking(cctv_list, depth + 1, arr_copy)

        arr_copy = deepcopy(current_arr)


back_tracking(cctv, 0, arr)
print(ans)




