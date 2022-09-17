# 220917 16987 계란으로 계란치기

# 정답코드

import sys
input = sys.stdin.readline

# N: 계란 개수
N = int(input())

# eggs: 계란
eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))

# broken: 계란 깨졌는지 여부 표시 배열
broken = [0 for _ in range(N)]

# ans: 깨진 게란의 최대 개수
ans = 0


# 백트래킹으로 깨진 계란의 개수 구하는 함수
def back_tracking(current):

    # 글로벌 변수 선언
    global ans

    # 마지막 계란까지 탐색 했을 때
    if current == N:
        # 정답 갱신 후 반환
        ans = max(sum(broken), ans)
        return

    # 현재 계란이 깨진 이미 계란일 경우
    elif broken[current] == 1:
        # 다음 계란으로 넘어간다.
        back_tracking(current + 1)

    # 현재 계란을 제외한 모든 계란이 깨졌을 경우
    elif broken[current] == 0 and sum(broken) == N - 1:
        # 바로 정답 갱신 후 반환
        ans = max(sum(broken), ans)
        return

    # pruning
    elif sum(broken) + (N - current) * 2 <= ans:
        return
 

    # 그 외 일반적인 경우
    else:
        for i in range(N):

            # 자신을 제외한 계란 중에서 선택
            if i == current:
                continue
            
            # 선택한 계란이 이미 깨졌을 경우 제외
            if broken[i] == 1:
                continue
            
            # 선택한 계란이랑 부딪히기
            eggs[current][0] -= eggs[i][1]
            eggs[i][0] -= eggs[current][1]

            # 깨졌는지 여부 검사
            if eggs[current][0] <= 0:
                broken[current] = 1

            if eggs[i][0] <= 0:
                broken[i] = 1

            # 다음 계란으로 넘어간다.
            back_tracking(current + 1)

            # 백트래킹
            eggs[current][0] += eggs[i][1]
            eggs[i][0] += eggs[current][1]

            broken[current] = 0
            broken[i] = 0


# 0번 계란부터 시작
back_tracking(0)

# 정답 출력
print(ans)
        

