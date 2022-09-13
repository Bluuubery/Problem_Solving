# 220914 5014 스타트링크

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

up_down = [U, - D]
building = [-1 for _ in range(F + 1)]


def bfs(start, end):
    building[start] = 0

    queue = deque()
    queue.append(start)

    while queue:
        floor = queue.popleft()
        if floor == end:
            print(building[floor])
            return
        else:
            for i in range(2):
                next_floor = floor + up_down[i]
                if 1 <= next_floor <= F:
                    if building[next_floor] == -1:
                        building[next_floor] = building[floor] + 1
                        queue.append(next_floor)


    if building[end] != -1:
        print(building[end])
    else:
        print('use the stairs')

    return


bfs(S, G)        
