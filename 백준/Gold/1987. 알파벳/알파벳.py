import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220925 1987 알파벳

# 정답코드

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = set(board[0][0],)

char_set = set()
for r in range(R):
    for c in range(C):
        char_set.add(board[r][c])

max_cnt = len(char_set)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


ans = 1


def back_tracking(r, c, cnt):
    global ans

    if cnt == max_cnt:
        print(max_cnt)
        exit(0)
    
        

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] not in visited:

                visited.add(board[nr][nc])

                back_tracking(nr, nc, cnt + 1)

                visited.remove(board[nr][nc])

    else:
        ans = max(ans, cnt)
        return

back_tracking(0, 0, 1)

print(ans)