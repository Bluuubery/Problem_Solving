from collections import deque


def solution(maps):
    answer = -1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    R = len(maps)
    C = len(maps[0])

    maps[0][0] = 2

    while queue:

        r, c = queue.popleft()

        if r == R - 1 and c == C - 1:
            answer = maps[r][c] - 1
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr, nc))


    return answer