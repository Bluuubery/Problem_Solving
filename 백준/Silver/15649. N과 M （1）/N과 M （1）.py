# 220915 15649 N과 M(1)

# 정답코드

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# sequence: 수열을 담을 배열 (0으로 초기화)
sequence = [0 for _ in range(M)]
# visited: 방문 여부 표시 배열
visited = [0 for _ in range(N + 1)]


# 백트래킹 함수 구현
def back_tracking(current):

    # 목표로하는 수열의 길이에 도달했을 경우
    if current == M:
        # 수열 출력 후 재귀 탈출
        for i in range(M):
            print(sequence[i], end=' ')
        print()
        return
    
    # 자연수 1 ~ N 탐색
    for i in range(1, N + 1):
        # 탐색 안한 수일 경우 해당 수를 수열에 넣어주고 방문 처리
        if visited[i] == 0:
            sequence[current] = i
            visited[i] = 1

            # 재귀적으로 다음 수 탐색
            back_tracking(current + 1)
            
            # 방문 여부 초기화
            visited[i] = 0


# 백트래킹으로 수열 출력
back_tracking(0)