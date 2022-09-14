# 220909 10816 숫자 카드

# 정답코드
from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

num_dict = defaultdict(int)

for i in range(N):
    num_dict[numbers[i]] += 1

for i in range(M):
    print(num_dict[targets[i]], end=' ')