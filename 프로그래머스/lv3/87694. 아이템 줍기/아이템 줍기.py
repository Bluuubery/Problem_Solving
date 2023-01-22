# 230122 아이템줍기

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 사각형
    board = [[0 for _ in range(102)] for _ in range(102)]
    
    
    # 좌표 (2배로 적용)
    for square in rectangle:
        c1, r1, c2, r2 = map(lambda x: x * 2, square)

        # 채우기
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                
                # 내부
                if r1 < r < r2 and c1 < c < c2:
                    board[r][c] = -1
                    
                # 테두리
                elif board[r][c] != -1:
                    board[r][c] = 1

                    
    # bfs 변수 설정 및 초기화
    queue = deque()
    queue.append((characterY * 2, characterX * 2, 0))

    visited = [[0 for _ in range(102)] for _ in range(102)]
    visited[characterY * 2][characterX * 2] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1] 

    
    while queue:
        
        r, c, dist = queue.popleft()

        # 종료 조건
        if r == itemY * 2 and c == itemX * 2:
            answer = dist
            break

        for i in range(4):

            nr = r + dr[i]
            nc = c + dc[i]
            
            # bfs 탐색
            if 0 <= nr < 102 and 0 <= nc < 102:
                if board[nr][nc] == 1 and not visited[nr][nc]:

                    visited[nr][nc] = 1

                    queue.append((nr, nc, dist + 1))

    # 정답 계산
    answer //= 2

    return answer