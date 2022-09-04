# 220905 2847 게임을 만든 동준이

# 정답 코드

import sys
input = sys.stdin.readline

# N: 레벨의 수
N = int(input())

# level: 각 레벨별 점수
level = []
for _ in range(N):
    level.append(int(input()))

# level을 뒤집어서 역순으로 검토한다.
level = level[::-1]

# ans: 바꾼 횟수
ans = 0
for i in range(1, N):
    # 직전 스테이지 점수가 더 높거나 같은 경우(역순 주의)
    if level[i] >= level[i - 1]:
        # 다음 스테이지 -1 점으로 점수를 낮춰주고 횟수를 세준다.
        ans += level[i] - level[i - 1] + 1 
        level[i] = level[i - 1] - 1

print(ans)