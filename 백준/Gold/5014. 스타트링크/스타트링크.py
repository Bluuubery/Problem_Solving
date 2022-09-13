# 220914 5014 스타트링크

# 정답코드

from collections import deque
import sys
input = sys.stdin.readline

# F: 건물 높이, S: 현재 위치, G: 목표 위치, U, D: 엘리베이터 위 아래
F, S, G, U, D = map(int, input().split())

# up_down: 엘리베이터 이동 정보 리스트 
up_down = [U, - D]
# building: bfs 탐색 시 방문 여부 및 엘리베이터 사용 횟수를 나타낼 리스트
building = [-1 for _ in range(F + 1)]


# bfs 함수 선언
def bfs(start, end):
    # 출발 지점 방문 및 엘리베이터 사용 횟수 표시
    building[start] = 0

    queue = deque()
    queue.append(start)

    while queue:
        floor = queue.popleft()

        # 목표 지점 도착 시 정답 출력 후 반환
        if floor == end:
            print(building[floor])
            return

        else:
            # 위 아래 이동 경우의 수 탐색
            for i in range(2):
                next_floor = floor + up_down[i]

                # 주어진 건물 높이 범위 내
                if 1 <= next_floor <= F:
                    # 미방문 층
                    if building[next_floor] == -1:
                        # 엘리베이터 사용 횟수 및 방문 여부 표시
                        building[next_floor] = building[floor] + 1

                        queue.append(next_floor)

    # 목표 지점 도착 시 정답 출력
    if building[end] != -1:
        print(building[end])
    # 도달 불가 시 문구 출력
    else:
        print('use the stairs')

    return


# bfs 탐색 실시
bfs(S, G)        
