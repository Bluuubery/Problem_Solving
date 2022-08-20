# 220820 2578 빙고

import sys

input = sys.stdin.readline

# bingo: 플레이어의 빙고판 숫자 배열
bingo = [list(map(int, input().split())) for _ in range(5)]

# call_number: 1차원 배열로 변환한 사회자가 부를 숫자 리스트
call_number = [list(map(int, input().split())) for _ in range(5)]
call_number = sum(call_number, [])


# 사회자가 부른 숫자의 인덱스를 찾는 함수
def find_index(a, array):
    for i in range(5):
        for j in range(5):
            if array[i][j] == a:
                return i, j


# 빙고 여부 검증 함수
def is_bingo(bingo):
    cnt = 0

    # 행 검증
    for row in bingo:
        if sum(row) == 0:
            cnt += 1

    # 열 검증
    for col in list(map(list, zip(*bingo[::-1]))):
        if sum(col) == 0:
            cnt += 1

    # 좌 -> 우 대각선 검증
    diagonal = 0
    for i in range(5):
        diagonal += bingo[i][i]
    if diagonal == 0:
        cnt += 1

    # 우 -> 좌 대각선 검증
    diagonal = 0
    for i in range(5):
        diagonal += bingo[i][4 - i]
    if diagonal == 0:
        cnt += 1

    # 3줄 이상일 경우 빙고
    if cnt >= 3:
        return True
    else:
        return False


# 카운트를 담을 변수
cnt = 0

while True:
    # 카운트 세주기
    cnt += 1

    # 사회자가 부른 숫자 지우기(0으로 초기화)
    i, j = find_index(call_number[cnt - 1], bingo)
    bingo[i][j] = 0

    # 빙고일시 루프 탈출
    if is_bingo(bingo):
        break
    else:
        pass

print(cnt)
