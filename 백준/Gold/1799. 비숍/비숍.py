import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220927 1799 비숍

# 정답코드

# N: 체스판의 크기, chess: 체스판의 초기 상태
N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]

# visited_diagonal 1, 2: 좌 -> 우, 우 ->좌 대각선 방문 여부 표시 배열 
visited_diagonal_1 = [0 for _ in range(2 * N)]
visited_diagonal_2 = [0 for _ in range(2 * N)]

# black, white: 비숍을 놓을 수 있는 위치를 체스판 색깔에 따라 구분한 좌표를 담은 배열
black = []
white = []
for r in range(N):
    for c in range(N):
        if chess[r][c]:
            if (r + c) % 2:
                black.append((r, c))
            else:
                white.append((r, c))


# 백트래킹으로 비숍 놓을 수 있는 위치 색깔별로 계산
def back_tracking(depth, cnt, candidates):
    global result
    
    # 해당 색깔 내의 모든 가능한 위치를 다 검증했을 경우 최댓값 갱신 후 반환
    if depth == len(candidates):
        result = max(result, cnt)
        return
    
    # r, c: 비숍을 놓을 수 있는지 여부를 검증할 위치의 좌표
    r, c = candidates[depth]
    
    # 해당 위치에 비숍을 놓을 수 있는 경우
    if visited_diagonal_1[r + c] == 0 and visited_diagonal_2[r - c + N] == 0:
        # 대각선 방문 여부 표시
        visited_diagonal_1[r + c] = 1
        visited_diagonal_2[r - c + N] = 1
        
        # 다음 위치 재귀적으로 탐색 진행
        back_tracking(depth + 1, cnt + 1, candidates)
        
        # 백트래킹
        visited_diagonal_1[r + c] = 0
        visited_diagonal_2[r - c + N] = 0

    # 놓을 수 없는 경우 놓지 않고 다음 위치 탐색 진행
    back_tracking(depth + 1, cnt, candidates)


# result: 해당 색에서 비숍을 놓을 수 있는 개수

# 흑과 백에 대해 각각 구해서 정답에 더해준다.
result = 0
back_tracking(0, 0, black)
ans = result

result = 0
back_tracking(0, 0, white)
ans += result

# 정답 출력
print(ans)