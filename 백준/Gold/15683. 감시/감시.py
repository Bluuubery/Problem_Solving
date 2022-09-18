from copy import deepcopy
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220918 15683 감시

# 정답코드

# N, M: 배열의 크기, arr: 사무실 상태 배열
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# direction_dict: cctv 감시 방향 정보
direction_dict = {
    1: [(0,), (1,), (2,), (3,)],
    2: [(0, 1), (2, 3)],
    3: [(0, 3), (3, 1), (1, 2), (2, 0)],
    4: [(2, 0, 3), (0, 3, 1), (3, 1, 2), (1, 2, 0)],
    5: [(0, 1, 2, 3)],
}


# K: cctv 개수, cctv: cctv의 인덱스를 담은 리스트, cctv_dict: 각 cctv의 번호를 담은 딕셔너리
K = 0
cctv = []
cctv_dict = dict()
for r in range(N):
    for c in range(M):
        if arr[r][c] != 0 and arr[r][c] != 6:
            cctv.append((r, c))
            cctv_dict[(r, c)] = arr[r][c]
            K += 1

# 델타 탐색 방향 설정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# ans: 사각지대 최소 크기 (큰 값으로 초기화)
ans = sys.maxsize


# cctv의 좌표와 감시 방향이 주어졌을 때 사무실을 감시하는 함수
def check(r, c, direction, arr_copy):
    # cctv의 감시 방향마다 감시
    for i in direction:
        nr, nc = r, c
        while True:
            nr += dr[i]
            nc += dc[i]

            # 범위를 벗어나거나 벽인 경우 감시 종료
            if not(0 <= nr < N and 0 <= nc < M) or arr[nr][nc] == 6:
                break

            # 빈 공간인 경우 감시
            elif arr[nr][nc] ==0:
                arr_copy[nr][nc] = 7

    return 
    

# 사무실의 상태가 주였을 때 사각지대를 세는 함수
def count_blind(arr):
    cnt = 0
    for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1
    return cnt


# 백트래킹을 통해 cctv를 회전시켜가며 감시하는 함수 
# current_arr: 현재 사무실의 감시 상태
def back_tracking(cctv_list, depth, current_arr):

    # 글로벌 변수 선언
    global ans

    # 모든 cctv에 대해서 검증을 마쳤을 경우
    if depth == K:
        # 정답 최솟값으로 갱신
        ans = min(ans, count_blind(current_arr))

        return

    # r, c: 현재 선택한 cctv의 좌표, cctv_type: 해당 cctv의 감시 방향
    r, c = cctv_list[depth]
    cctv_type = cctv_dict[(r, c)]

    # arr_copy: 사무실 상태의 복사본 배열
    arr_copy = deepcopy(current_arr)

    # cctv를 회전 시켜가며 탐색 실시
    for direction in direction_dict[cctv_type]:
        # 현재 회전시킨 방향으로 cctv 감시 
        check(r, c, direction, arr_copy)

        # 다음 cctv로 넘어감
        back_tracking(cctv_list, depth + 1, arr_copy)

        # 백트래킹 위해 사무실 상태 원복
        arr_copy = deepcopy(current_arr)


# 0번째 cctv부터 탐색
back_tracking(cctv, 0, arr)

# 정답 출력
print(ans)
