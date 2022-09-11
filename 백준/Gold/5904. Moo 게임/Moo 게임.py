# 220911 5904 Moo게임

# 정답코드
import bisect
from posixpath import split
import sys
input = sys.stdin.readline




# 무 수열 어디에 위치해있는지 찾는 함수
def split_moo(N, K):
    if K == 0:
        if N == 1:
            print('m')
        else:
            print('o')
        return

    # S(K - 1) 처음
    if 0 <= N < moo_len[K - 1]:
        split_moo(N, K - 1)
    
    # 가운데
    elif moo_len[K - 1] <= N < moo_len[K - 1] + K + 3:
        # print(f'중간{N, K}')
        if N - moo_len[K - 1] == 1:
            print('m')
        else:
            print('o')
        return

    # S(K - 1) 끝
    else:
        split_moo(N - (moo_len[K - 1] + K + 3), K - 1)


moo_len = [3]

for i in range(1, 28):
    next_moo = moo_len[-1] * 2 + (i + 3)
    moo_len.append(next_moo)

N = int(input())

# N이 몇 번쨰 무인지 찾기
K = bisect.bisect_left(moo_len, N)


# print(N, K)
split_moo(N, K)

# if split_moo(N, K) == 1:
#     print('m')
# else:
#     print('o')