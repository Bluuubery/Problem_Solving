# 220912 18869 멀티버스II

# 정답코드

from collections import defaultdict
import sys
input = sys.stdin.readline

# N: 우주의 개수, M: 우주에 있는 행성의 개수
N, M = map(int, input().split())


# 해시를 이용한 좌표 압축 함수
def compression(numbers):
    
    numbers_set = sorted(list(set(numbers)))
    num_dict = defaultdict(int)

    for i in range(len(numbers_set)):
        num_dict[numbers_set[i]] = i
    
    compressed = []
    for i in numbers:
        compressed.append(num_dict[i])
    
    # 딕셔너리의 키로 사용하기 위해 튜플 형태로 반환
    return tuple(compressed)


# multiverse: 각 우주의 인덱스 순서를 담을 딕셔너리
multiverse = defaultdict(int)
# 각 우주의 행성 크기를 좌표 압축 후 딕셔너리에 삽입
for i in range(N):
    universe = list(map(int, input().split()))
    univ_idx = compression(universe)
    multiverse[univ_idx] += 1

# cnt: 우주의 쌍 개수
cnt = 0
# 균등한 우주가 2 개 이상일 때 우주의 쌍 개수를 계산해서 더해준다.
for v in multiverse.values():
    if v >= 2:
        cnt += v * (v - 1) // 2

# 정답 출력
print(cnt)