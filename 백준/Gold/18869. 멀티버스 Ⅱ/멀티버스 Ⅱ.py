# 220912 18869 멀티버스II

# 정답코드

from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())


# 좌표 압축 함수
def compression(numbers):
    
    numbers_set = sorted(list(set(numbers)))
    num_dict = defaultdict(int)

    for i in range(len(numbers_set)):
        num_dict[numbers_set[i]] = i
    
    compressed = []
    for i in numbers:
        compressed.append(num_dict[i])
    
    return tuple(compressed)


multiverse = defaultdict(int)
for i in range(N):
    universe = list(map(int, input().split()))
    univ_idx = compression(universe)
    multiverse[univ_idx] += 1

cnt = 0
for v in multiverse.values():
    if v >= 2:
        cnt += v * (v - 1) // 2

print(cnt)