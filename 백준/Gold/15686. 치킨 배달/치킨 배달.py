# 220904 15686 치킨 배달

import sys
from itertools import combinations
input = sys.stdin.readline

# N: 도시 배열의 크기, M: 남길 치킨 집 개수, arr: 도시의 배열 
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# chicken: 현재 있는 치킨집 위치, home: 도시 내 집들의 위치
chicken = []
home = []
# 현재 도시 내에 치킨집과 집들의 위치를 각각 리스트에 담아준다.
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            home.append((r, c))
        elif arr[r][c] == 2:
            chicken.append((r, c))

# ans: 정답을 담을 변수(충분히 큰 값으로 초기화)
ans = 99999
# 조합을 이용해 가능한 치킨집 경우의 수를 모두 구해 반복문
for left_chickens in combinations(chicken, M):
    # chicken_distance: 도시 전체 치킨 거리
    chicken_distance = 0

    # 각 집마다 치킨 거리를 구한다.
    for house in home:
        # min_distance: 한 집의 치킨 거리(충분히 큰 값으로 초기화)
        min_distance = 99999
        
        # 모든 치킨집의 치킨 거리를 구한 뒤 계속 비교해가며 최솟값을 구한다.
        for i in range(M):
            distance = abs(house[0] - left_chickens[i][0]) + abs(house[1] - left_chickens[i][1])
            if distance < min_distance:
                min_distance = distance

        # 도시 전체 치킨 거리에 더해주기
        chicken_distance += min_distance
    
    # 현재 최소 치킨 거리랑 비교해가면서 갱신
    if chicken_distance < ans:
        ans = chicken_distance

print(ans)
            