# 210122 퍼즐조각채우기


from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(board, r, c, visited, target, N):
    '''
    board: 배열 종류 (게임 / 테이블)
    r, c: 좌표
    visited: 해당 배열의 방문 표시 배열
    target: 해당 배열에서 찾고자 하는 숫자
    N: 배열 크기
    '''

    # result: 블럭 좌표 담을 배열
    result = [(r, c)]
    visited[r][c] = 1

    queue = deque()
    queue.append((r, c))
    
    # bfs 탐색으로 블럭 좌표들 찾아서 반환
    while queue:

        r, c = queue.popleft()

        for i in range(4):

            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and board[nr][nc] == target:

                    queue.append((nr, nc))
                    visited[nr][nc] = 1

                    result.append((nr, nc))
    
    return result


# 블럭 정렬 후 재배치
def sort_block(block: list):

    # 정렬
    block.sort()

    min_r = min([b[0] for b in block])
    min_c = min([b[1] for b in block])

    # 블럭 간 비교 위해 가장 작은 좌표 기준으로 재배치
    block = list(map(lambda x: (x[0] - min_r, x[1] - min_c), block))

    return block


# 블럭 회전
def rotate_block(block: list, N):

    # 한 조각 블럭은 그대로 반환
    if len(block) == 1:
        return block

    # blocks: 회전된 블럭들을 담을 배열
    blocks = [block]

    # 90, 180, 270도 회전+정렬 
    for i in range(3):
        block = list(map(lambda x: (x[1], N - 1 - x[0]), block))

        block = sort_block(block)
        blocks.append(block)

    # 블럭 간 비교 위해 가장 작은 좌표의 블럭 한 개만 반환
    return min(blocks)



def solution(game_board, table):

    # 변수 설정 및 초기화
    answer = 0

    N = len(game_board)

    # 방문 여부 표시 배열
    visited_board = [[0 for _ in range(N)] for _ in range(N)]
    visited_table = [[0 for _ in range(N)] for _ in range(N)]
    
    # 블럭 담을 배열
    block_board = []
    block_table = []

    for r in range(N):
        for c in range(N):

            # board
            if not visited_board[r][c] and game_board[r][c] == 0:

                block = bfs(game_board, r, c, visited_board, 0, N) # 블럭 탐색
                block = sort_block(block) # 정렬 후 재배치
                block = rotate_block(block, N) # 회전

                block_board.append(block)
            
            # table
            if not visited_table[r][c] and table[r][c] == 1:

                block = bfs(table, r, c, visited_table, 1, N)
                block = sort_block(block)
                block = rotate_block(block, N)

                block_table.append(sort_block(block))

    # 퍼즐 조각 채울 때 중복 여부 검사용 배열
    checked_board = [0 for _ in range(len(block_board))]


    for block in block_table:
        for i in range(len(block_board)):
            
            # 이미 채웠을 경우
            if checked_board[i]:
                continue
            
            # 채울 수 있는 경우
            if block == block_board[i]:
                answer += len(block)
                checked_board[i] = 1
                break
                    
    return answer