# 220828 1974 스도쿠검증

T = int(input())

# in 연산자를 통해서 스도쿠를 검증한다.(합은 예외가 있을 수 있음!)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for t in range(1, T + 1):
    # sudoku: 스도쿠 숫자 배열
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # flag: 스도쿠 여부
    flag = 1

    # 행, 열 검증
    for i in range(9):
        # row: 행, col: 열
        row = []
        col = []
        for j in range(9):
            row.append(sudoku[i][j])
            col.append(sudoku[j][i])
        # 1 ~ 9 중 빠진 숫자가 있으면 스도쿠가 아니다.
        for number in numbers:
            if number not in col:
                flag = 0
            if number not in row:
                flag = 0

    # 사각형 영역 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for k in range(3):
                square.append(sudoku[i][j + k])
                square.append(sudoku[i + 1][j + k])
                square.append(sudoku[i + 2][j + k])
            for number in numbers:
                if number not in square:
                    flag = 0
    
    # 스도쿠 여부를 양식에 맞게 출력한다.
    print('#{} {}'.format(t, flag))