from collections import deque
from itertools import count
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220918 1941 소문난 칠공주

# 정답코드

students = [list(map(str, input())) for _ in range(5)]
visited = [0 for _ in range(25)]

princess = []

cnt = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]



def is_adjacent(princess):
    visited_adjacent = [[0 for _ in range(5)] for _ in range(5)]

    r = princess[0] // 5
    c = princess[0] % 5

    queue = deque()
    queue.append((r, c))
    visited_adjacent[r][c] = 1
    cnt = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if 0 <= nr < 5 and 0 <= nc < 5 and visited_adjacent[nr][nc] == 0:
                if nr * 5 + nc in princess:
                    visited_adjacent[nr][nc] = 1
                    cnt += 1

                    queue.append((nr, nc))
    
    if cnt == 7:
        return True
    
    return False





def count_y(princess):
    cnt = 0
    for rc in princess:
        r = rc // 5
        c = rc % 5
        if students[r][c] == 'Y':
            cnt += 1

        if cnt > 3:
            return False

    return True





def backtracking(current, depth):
    global cnt

    if not count_y(princess):
        return


    if depth == 7:
        if is_adjacent(princess):
            cnt += 1
            # print('yes: ', cnt, princess)
        # else:
            # print('no: ', princess)

        return

    for i in range(current, 25):

        princess.append(i)

        backtracking(i + 1, depth + 1)

        # for j in range(i + 1, 25):
        #     visited[j] = 0

        princess.pop()


backtracking(0, 0)

print(cnt)
# princess = [5, 6, 7, 8, 9, 14, 19]
# print(students)
# print(count_y(princess))
# print(is_adjacent(princess))