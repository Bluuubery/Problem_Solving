# 220915 15657 N과 M (8)

# 정답코드

import sys
input = sys.stdin.readline

# N: 수열의 범위, M: 수열의 길이, numbers: 탐색할 수열
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

# sequence: 결과 수열을 담을 배열
# result: 결과 수열들을 담을 배열
sequence = []
result = set()

# visited: 방분 여부 표시 배열
visited = [0 for _ in range(N)]


# 백트래킹 함수 구현
def back_tracking():

    # 수열의 길이가 M에 도달했을 때
    if len(sequence) == M:
        # result 배열에 중복이 없으면 복사본을 넣고 재귀 탈출
        result.add(tuple(sequence))
        return

    for i in range(N):
        # 방문하지 않았을 경우
        if visited[i] == 0:

            # 선택한 수 수열에 삽입 후 방문 표시
            sequence.append(numbers[i])
            visited[i] = 1

            # 재귀적으로 반복
            back_tracking()

            # 백트래킹 위해 수열에서 수 빼주기, 방문 여부 초기화
            sequence.pop()
            visited[i] = 0

    return 


# 백트래킹으로 수열 담아주기
back_tracking()

# 수열들을 하나씩 출력해준다.
for sub in sorted(list(result)):
    print(*sub)