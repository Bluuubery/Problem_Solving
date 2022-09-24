# 220915 1182 부분수열의 합

# 정답코드

import sys
input = sys.stdin.readline

# N: 수열의 길이, S: 찾고자 하는 수
N, S = map(int, input().split())
# numbers: 수열
numbers = list(map(int, input().split()))

# cnt: 합이 s가 되는 부분수열의 개수
cnt = 0


# 백트래킹 함수 선언
def backtracking(current,total, S):

    # 글로벌 변수 선언
    global cnt

    # 원소를 다 선택했을 때
    if current == N:
        # 부분수열의 합이 s면 정답을 세준다.
        if total == S:
            cnt += 1
        return

    # 주어진 수열에 대해서 해당 수를 선택하지 않은 경우 재귀적 탐색
    backtracking(current + 1, total, S)
    # 주어진 수열에 대해서 해당 수를 선택한 경우 재귀적 탐색
    backtracking(current + 1, total + numbers[current], S) 


# 0부터 백트래킹 실시
backtracking(0, 0, S)

# 정답 출력
# S가 0이면 공집합 1개를 빼준다.
if S == 0:
    print(cnt - 1)
else:
    print(cnt)