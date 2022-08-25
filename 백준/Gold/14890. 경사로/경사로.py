# 220825 14890 활주로 건설
 
# 정답 코드
 
# 지형의 높이차를 구하는 함수 선언
def height_diff(arr, N):
    height_diff = [[] for _ in range(N)]
 
    for i in range(N):
        # 각 행에서 첫번째는 0을 넣어준다.
        height_diff[i].append(0)
        # 직전 항과의 높이차
        for j in range(1, N):
            height_diff[i].append(arr[i][j] - arr[i][j - 1])
 
    return height_diff
 
 
# 가능한 경사로 설치 개수 확인하는 함수 선언 (행에 대해서만 검사)
def check_runway(height_diff, N, L):
    cnt = 0
    # 경사로 설치 여부만을 표시할 빈 N * N 배열 (중복 설치 확인용)
    constructed = [[0] * N for _ in range(N)]
 
    for row in range(N):
        for col in range(N):
            # 높이차가 0(평탄)이면 continue
            if height_diff[row][col] == 0:
                continue
             
            # 높이차가 1: 이전보다 높은 지형 -> 왼쪽으로 경사로 설치(자신 제외)
            elif height_diff[row][col] == 1:
 
                # 자기 자신을 제외하고 왼쪽으로 L 길이 설치 가능 여부 검증
                for i in range(1, L + 1):
                    # 범위를 벗어나거나 평탄하지 않은 경우 제외
                    if col - i < 0 or height_diff[row][col - i] != 0:
                        break
                    # 이미 경사로를 설치한 경우 제외
                    if constructed[row][col - i]:
                        break
 
                # 경사로 설치 가능
                else:
                    # 경사로를 설치했으므로 해당 높이차를 0으로 바꿔준다.(평탄화)
                    height_diff[row][col] = 0
                    # 경사로를 설치한 영역에 표시를 해준다. (자신 제외 왼쪽으로 L)
                    for i in range(1, L + 1):
                        constructed[row][col - i] = 1
 
            # 놀이차가 -1: 이전보다 낮은 지형 -> 오른쪽으로 경사로 설치(자신 포함)
            elif height_diff[row][col] == -1:
 
                # 오른쪽으로 (L - 1)길이 검증 (자신은 검증x)
                for i in range(1, L):
                    if col + i >= N or height_diff[row][col + i] != 0:
                        break
                    if constructed[row][col + i]:
                        break
 
                # 경사로 설치 가능
                else: 
                    # 경사로 설치
                    height_diff[row][col] = 0
                    # 경사로를 설치한 영역에 표시를 해준다. (자신 포함 오른쪽으로 L)
                    for i in range(0, L):
                        constructed[row][col + i] = 1
 
            # 높이차의 절댓값이 1보다 큰 경우: 설치 불가
            else:
                break
            # 행 전체 검증 후 높이차가 남아 있으면 제외
            if height_diff[row][col] != 0:
                break
         
        # 높이차가 없으면(경사로 설치 or 원래 활주로 건설 가능) 카운트를 세준다.
        else:
            cnt += 1
     
    # 총 활주로 개수 반환
    return cnt
 

# N: 배열 크기, L: 경사로 길이, ans: 가능한 활주로 건설 개수
N, L = map(int, input().split())
ans = 0

# arr: 지도 배열, arr: 지도 내 각 지역의 높이 차 배열
arr = [list(map(int, input().split())) for _ in range(N)]
arr_height_diff = height_diff(arr, N)

# 행 검증시 활주로 개수 가산
ans += check_runway(arr_height_diff, N, L)
 
# rotate_arr: 시계방향으로 90도 회전한 배열, rotate_arr_height_diff: 회전한 배열의 높이차
rotate_arr = list(map(list, zip(*arr[::-1])))
rotate_arr_height_diff = height_diff(rotate_arr, N)

# 열 검증시 활주로 개수 가산
ans += check_runway(rotate_arr_height_diff, N, L)

print(ans)