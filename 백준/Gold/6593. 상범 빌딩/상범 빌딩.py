from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220918 6593 상범 빌딩

# 정답코드

dh = [0, 0, 0, 0, -1, 1]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]



def bfs(h, r, c, building):

    queue = deque()
    building[h][r][c] = 0
    queue.append((h, r, c))

    while queue:
        h, r, c = queue.popleft()

        for i in range(6):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nh < L and 0 <= nr < R and 0 <= nc < C:
                if building[nh][nr][nc] == '.':
                    building[nh][nr][nc] = building[h][r][c] + 1
                    queue.append((nh, nr, nc))
                
                elif building[nh][nr][nc] == 'E':
                    ans = building[h][r][c] + 1
                    print(f'Escaped in {ans} minute(s).')
                    return

    print('Trapped!')
    return





while True:
    L, R, C = list(map(int, input().split()))
    if L == R == C == 0:
        break


    building = []

    for _ in range(L):
        building.append([list(map(str, input())) for _ in range(R)])
        input()

    for l in range(L):
        for r in range(R):
            for c in range(C):
                if building[l][r][c] == 'S':
                    bfs(l, r, c, building)

    
