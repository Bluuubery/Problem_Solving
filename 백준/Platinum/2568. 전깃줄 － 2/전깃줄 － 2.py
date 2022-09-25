from bisect import bisect_left
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220925 2569 전깃줄 - 2

# 정답코드

N = int(input())

wire = []
for _ in range(N):
    wire.append(list(map(int, input().split())))


wire.sort(key=lambda x:x[0])


# lis_temp: 임시 lis
# lis_idx: 각 수의 lis에서의 idx를 담을 리스트
lis_temp = []
lis_idx = []

# 이분탐색을 통해 수열의 수가 lis에 들어갈 위치를 찾는다.
for i in range(N):
    # idx: 수가 들어갈 위치
    idx = bisect_left(lis_temp, wire[i][1])
    lis_idx.append(idx)
    # 현재 lis의 길이보다 뒤쪽이면 임시 lis에 추가해준다.
    if len(lis_temp) <= idx:
        lis_temp.append(wire[i][1])
    # 들어갈 위치에 있는 수와 대체
    else:
        lis_temp[idx] = wire[i][1]

# lis_idx에 저장해둔 인덱스를 거꾸로 탐색해서 lis를 채워나간다.
max_idx = max(lis_idx)
lis = []
for i in range(N - 1, -1, -1):
    if lis_idx[i] == max_idx:
        lis.append(wire[i][1])
        max_idx -= 1

# # 거꾸로된 lis를 다시 정방향으로 뒤집어준다.
# lis.reverse()
print(N - len(lis))

# print(lis)
# print(wire)
for i in range(N):
    if wire[i][1] not in lis:
        print(wire[i][0])