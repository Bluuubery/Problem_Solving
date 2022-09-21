import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220921 2239 스도쿠

# 정답코드

N = 9
board = [list(map(int, input())) for _ in range(N)]


def find_square(r, c):
    return (r // 3) * 3+ (c // 3)


def get_idx(num):
    r = num // 9
    c = num % 9
    return r, c


def back_tracking(depth):

    if depth == 81:
        for i in board:
            print(''.join(map(str, i)))
        exit(0)

    r, c = get_idx(depth)

    if board[r][c]:
        back_tracking(depth + 1)

    else:
        for num in numbers:
            if not visited_row[r][num] and not visited_col[c][num] and not visited_square[find_square(r, c)][num]:

                board[r][c] = num
                visited_row[r][num] = 1
                visited_col[c][num] = 1
                visited_square[find_square(r, c)][num] = 1

                back_tracking(depth + 1)

                board[r][c] = 0
                visited_row[r][num] = 0
                visited_col[c][num] = 0
                visited_square[find_square(r, c)][num] = 0
        else:
            return


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
visited_row = [[0 for _ in range(10)] for _ in range(10)]
visited_col = [[0 for _ in range(10)] for _ in range(10)]
visited_square = [[0 for _ in range(10)] for _ in range(10)]

for r in range(9):
    for c in range(9):
        if board[r][c]:
            visited_row[r][board[r][c]] = 1
            visited_col[c][board[r][c]] = 1
            visited_square[find_square(r, c)][board[r][c]] = 1


back_tracking(0)

