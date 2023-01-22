# 210122 퍼즐조각채우기


from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(board, r, c, visited, target, N):
    result = [(r, c)]
    visited[r][c] = 1

    queue = deque()
    queue.append((r, c))

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


def sort_block(block: list):
    block.sort()
    min_r = min([b[0] for b in block])
    min_c = min([b[1] for b in block])

    block = list(map(lambda x: (x[0] - min_r, x[1] - min_c), block))

    return block


def rotate_block(block: list, N):
    if len(block) == 1:
        return block

    blocks = [block]

    for i in range(3):
        block = list(map(lambda x: (x[1], N - 1 - x[0]), block))
        block = sort_block(block)
        blocks.append(block)

    return min(blocks)



def solution(game_board, table):
    answer = 0

    N = len(game_board)

    visited_board = [[0 for _ in range(N)] for _ in range(N)]
    visited_table = [[0 for _ in range(N)] for _ in range(N)]
    
    block_board = []
    block_table = []

    for r in range(N):
        for c in range(N):
            if not visited_board[r][c] and game_board[r][c] == 0:
                block = bfs(game_board, r, c, visited_board, 0, N)
                block = sort_block(block)
                block = rotate_block(block, N)
                block_board.append(block)
            
            if not visited_table[r][c] and table[r][c] == 1:
                block = bfs(table, r, c, visited_table, 1, N)
                block = sort_block(block)
                block = rotate_block(block, N)
                block_table.append(sort_block(block))

    checked_board = [0 for _ in range(len(block_board))]
    # checked_table = [0 for _ in range(len(block_table))]

    # for b in block_table:
    #     print(b)

    # print()

    # for b in block_board:
    #     print(b)
    # print(block_table)

    for block in block_table:
        for i in range(len(block_board)):

            if checked_board[i]:
                continue

            if block == block_board[i]:
                answer += len(block)
                checked_board[i] = 1
                break
                    
    # print()

    # print(answer)
    return answer