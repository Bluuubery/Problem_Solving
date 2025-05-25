# 230122 여행경로


def solution(tickets):

    # 변수 설정 및 초기화
    answer = []
    N = len(tickets)
    visited = [0 for _ in range(N)]


    # 백트래킹 함수 선언
    def backtracking(depth: int, current: str, route:list):
        nonlocal N, answer


        # 반환 조건
        if depth == N:
            if not answer or answer >= route:
                answer = route
            return

        # 백트래킹
        for i in range(N):

            if not visited[i] and tickets[i][0] == current:
                visited[i] = 1
                backtracking(depth + 1, tickets[i][1], route + [tickets[i][1]])
                visited[i] = 0

    backtracking(0, 'ICN', ['ICN'])


    return answer
