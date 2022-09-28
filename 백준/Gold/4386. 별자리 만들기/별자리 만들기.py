from itertools import combinations
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220928 4386 별자리 만들기

# 정답코드

N = int(input())

# parent: 부모 테이블 (자기 자신으로 초기화)
parent = [i for i in range(N + 1)]


# find 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# union 함수
def merge(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
        
    else:
        parent[x] = y

    return

stars = []
total_cost = 0

# 별의 위치 정보  
for i in range(1, N + 1):
    stars.append([i] + list(map(float, input().split())))

# 별 간 간성 정보
stars_weight = []
for star_1, star_2 in combinations(stars, 2):
    star_1_idx, star_1_x, star_1_y = star_1[0], star_1[1], star_1[2]
    star_2_idx, star_2_x, star_2_y = star_2[0], star_2[1], star_2[2]
    weight = (abs(star_1_x - star_2_x) ** 2 + abs(star_1_y - star_2_y) ** 2) ** (1/2)
    stars_weight.append((weight, star_1_idx, star_2_idx))


# 가중치 기준으로 정렬
stars_weight.sort()


# 각 간선에 대해 유니온-파인드로 cylce 여부 판단하여 크루스칼 알고리즘 수행
for i in range(len(stars_weight)):
    cost, node1, node2 = stars_weight[i]
    # 부모 노드가 다르면 cylce하지 않다
    if find(node1) != find(node2):
        # mst에 포함
        merge(node1, node2)
        # 가중치 계산
        total_cost += cost


# # 가중치 합계 출력
print(round(total_cost, 2))

