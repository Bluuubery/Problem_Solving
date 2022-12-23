import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 221224 2072 오목

# 정답코드

def check_five(r, c):
    
    num = board[r][c]

    max_len = 0
    cnt = 0
    for i in range(r - 4, r + 5):
        if 0 <= i < 19:
            if board[i][c] == num:
                cnt += 1
                max_len = max(cnt, max_len)
            else:
                cnt = 0

    if max_len == 5:
        return True

    max_len = 0
    cnt = 0
    for i in range(c - 4, c + 5):
        if 0 <= i < 19:
            if board[r][i] == num:
                cnt += 1
                max_len = max(cnt, max_len)
            else:
                cnt = 0

    if max_len == 5:
        return True

    max_len = 0
    cnt = 0
    for i in range(-4, 5):
        if 0 <= r + i < 19 and 0 <= c + i < 19:
            if board[r + i][c + i] == num:
                cnt += 1
                max_len = max(cnt, max_len)
            else:
                cnt = 0
    
    if max_len == 5:
        return True

    max_len = 0
    cnt = 0
    for i in range(-4, 5):
        if 0 <= r + i < 19 and 0 <= c - i < 19:
            if board[r + i][c - i] == num:
                cnt += 1
                max_len = max(cnt, max_len)
            else:
                cnt = 0

    if max_len == 5:
        return True

    return False
    


board = [[0 for _ in range(19)] for _ in range(19)]

N = int(input())
ans = -1

for i in range(1, N + 1):
    r, c = map(int, input().split())

    r -= 1
    c -= 1

    if i % 2:
        board[r][c] = 1
    else:
        board[r][c] = 2

    if check_five(r, c):
        print(i)
        exit()

# for row in board:
#     print(row)

print(ans)