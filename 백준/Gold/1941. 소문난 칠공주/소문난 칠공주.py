from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220918 1941 소문난 칠공주

# 정답코드

# students: 학생들 자리 배치 배열
students = [list(map(str, input())) for _ in range(5)]

# princess: 칠공주파 idx를 담을 배열 
princess = []

# cnt: 소문난 칠공주 결성 가능 경우의 수
cnt = 0

# 델타 탐색 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 결성된 칠공주가 서로 인접해있는지 검증하는 함수
def is_adjacent(princess):
    # visited: 방문 여부 표시 배열
    visited = [[0 for _ in range(5)] for _ in range(5)]

    # 인덱스를 2차원 배열의 인덱스로 바꿔줌
    r = princess[0] // 5
    c = princess[0] % 5

    queue = deque()
    queue.append((r, c))
    
    # 방문 표시 및 인접 인원 세주기
    visited[r][c] = 1
    cnt = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # 인덱스 범위를 벗어나지 않고 미방문일 경우
            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc] == 0:
                # 현재 선택한 칠공주파에 속해있을 경우
                if nr * 5 + nc in princess:
                    # 방문 표시 및 인접 인원 세주기
                    visited[nr][nc] = 1
                    cnt += 1

                    queue.append((nr, nc))
    
    # 7명의 칠공주파가 서로 인접해있을 경우 True 반환
    if cnt == 7:
        return True
    
    # 서로 인접해있지 않을 경우 False 반환
    return False


# 가지치기를 위해 이다솜파의 인원을 세는 함수
def count_y(princess):
    # cnt: 이다솜파의 인원
    cnt = 0

    # 이다솜파 인원 세주기
    for rc in princess:
        r = rc // 5
        c = rc % 5
        if students[r][c] == 'Y':
            cnt += 1

        # 이다솜파가 4명 이상일 경우 True
        if cnt > 3:
            return True

    # 3명 이하일 경우 False
    return False


# 칠공주파 결성하는 백트래킹 함수 선언
def backtracking(current, depth):
    # 결성된 칠공주파의 수 세는 글로벌 변수 선언
    global cnt

    # 가지치기: 만약 중간에 이다솜파가 4명 이상일 경우 반환
    if count_y(princess):
        return

    # 7명이 모였을 때 서로 인접해있는지 검증 후 반환
    if depth == 7:
        if is_adjacent(princess):
            cnt += 1
        return

    # 5 * 5 배열의 인덱스를 1차원 배열의 인덱스 변환해서 7명 뽑는 경우의 수
    for i in range(current, 25):

        princess.append(i)

        backtracking(i + 1, depth + 1)

        princess.pop()


# 칠공주파 탐색
backtracking(0, 0)

# 전체 칠공주파 수 출력
print(cnt)
