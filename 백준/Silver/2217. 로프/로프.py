# 220904 2217 로프

# 정답코드

import sys
input = sys.stdin.readline

# N: 로프의 개수 
N = int(input())

# rope: 각 로프가 견딜 수 있는 하중
rope = []
for _ in range(N):
    rope.append(int(input()))

# 로프의 하중을 오름차순으로 정렬한다.
rope.sort()

# 여러 로프가 견딜 수 있는 무게 = 가장 낮은 하중의 로프 * 로프의 갯수
# 각 로프 별로 경우의 수를 구해서 최댓값을 찾는다.
max_weight = 0
for i in range(N):
    weight = rope[i] * (N - i)
    if weight > max_weight:
        max_weight = weight

print(max_weight)